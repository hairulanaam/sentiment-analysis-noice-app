import plotly.graph_objects as go
import streamlit as st
from config import FONT_FAMILY, NEGATIVE_COLOR, NEUTRAL_COLOR, POSITIVE_COLOR


def reviews_card(total):
    with st.container(border=True, key="reviews_card_container"):
        st.markdown(
            f"""
            <div style="text-align:center;">
                <div class="top-bar-label">Reviews</div>
                <div class="top-bar-value" style="margin-top: 4px;">{total:,}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

def sentiment_breakdown(counts):
    with st.container(border=True, key="breakdown_card_container"):
        st.markdown(
            '<div class="section-header">Sentiment Breakdown</div>',
            unsafe_allow_html=True,
        )

        labels = ['Positive', 'Neutral', 'Negative']
        values = [counts['positive'], counts['neutral'], counts['negative']]
        colors = [POSITIVE_COLOR, NEUTRAL_COLOR, NEGATIVE_COLOR]

        fig = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            hole=0.55,
            marker=dict(
                colors=colors,
                line=dict(color='white', width=2.5),
            ),
            textinfo='percent',
            textposition='inside',
            textfont=dict(size=14, color='white', family=FONT_FAMILY),
            hovertemplate=(
                '%{label}<br>Count: %{value:,}<br>'
                'Percent: %{percent}<extra></extra>'
            ),
            sort=False,
            direction='clockwise',
            rotation=90,
        )])

        fig.update_layout(
            showlegend=False,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=10, r=10, t=10, b=10),
            height=250,
        )

        st.plotly_chart(fig, use_container_width=True, key="sentiment_donut")
