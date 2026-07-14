import pandas as pd
import streamlit as st
from collections import Counter
from config import DATASET_PATH

@st.cache_data
def load_data():
    df = pd.read_csv(DATASET_PATH)
    df['at'] = pd.to_datetime(df['at'])
    df = df.dropna(subset=['at', 'polarity'])
    return df


def filter_by_date(df, start_date, end_date):
    return df[
        (df['at'].dt.date >= start_date) & (df['at'].dt.date <= end_date)
    ].copy()


def compute_polarity_counts(df_filtered):
    total = len(df_filtered)
    counts = df_filtered['polarity'].value_counts()
    pos = counts.get('positive', 0)
    neu = counts.get('neutral', 0)
    neg = counts.get('negative', 0)

    if total > 0:
        pos_pct = (pos / total) * 100
        neu_pct = (neu / total) * 100
        neg_pct = (neg / total) * 100
    else:
        pos_pct = neu_pct = neg_pct = 0.0

    return {
        'total': total,
        'positive': pos,
        'neutral': neu,
        'negative': neg,
        'pos_pct': pos_pct,
        'neu_pct': neu_pct,
        'neg_pct': neg_pct,
    }


def compute_trend_data(df_filtered):
    df_work = df_filtered.copy()
    df_work['month'] = df_work['at'].dt.to_period('M')
    trend_df = (
        df_work
        .groupby(['month', 'polarity'])
        .size()
        .unstack(fill_value=0)
    )

    for c in ['positive', 'neutral', 'negative']:
        if c not in trend_df.columns:
            trend_df[c] = 0

    trend_df = trend_df[['positive', 'neutral', 'negative']].sort_index()
    trend_df.index = trend_df.index.to_timestamp()
    return trend_df


def compute_top_words(df_filtered, n=10):
    non_empty = df_filtered['text_final'].dropna().astype(str)
    if len(non_empty) == 0:
        return None

    all_words = []
    for text in non_empty:
        all_words.extend(text.split())

    if len(all_words) == 0:
        return None

    word_counts = Counter(all_words)
    top_n = word_counts.most_common(n)
    top_df = pd.DataFrame(top_n, columns=['Word', 'Frequency'])
    top_df = top_df.sort_values(by='Frequency', ascending=True)
    return top_df
