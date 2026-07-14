from pathlib import Path
import streamlit as st
from components.filters import date_filter
from components.header import header
from components.sentiment_breakdown import sentiment_breakdown, reviews_card
from components.sentiment_trend import sentiment_trend
from components.top_words_chart import top_words
from components.wordcloud_chart import wordcloud_chart
from utils.data_loader import (
    compute_polarity_counts,
    filter_by_date,
    load_data,
)

st.set_page_config(
    page_title="Sentimen Analysis",
    layout="wide",
    initial_sidebar_state="collapsed",
)
css_path = Path(__file__).parent / "styles" / "dashboard.css"
st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)

try:
    df = load_data()
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

min_date = df['at'].min().date()
max_date = df['at'].max().date()

header()

col_left, col_right = st.columns([1.2, 2])
with col_left:
    col_sub_date, col_sub_reviews = st.columns([1.3, 1])
    with col_sub_date:
        start_date, end_date = date_filter(min_date, max_date)
    df_filtered = filter_by_date(df, start_date, end_date)
    counts = compute_polarity_counts(df_filtered)
    with col_sub_reviews:
        reviews_card(counts['total'])
    sentiment_breakdown(counts)

with col_right:
    sentiment_trend(df_filtered, counts['total'])
col_wordcloud, col_top_words = st.columns([1, 1])
with col_wordcloud:
    wordcloud_chart(df_filtered)
with col_top_words:
    top_words(df_filtered)
