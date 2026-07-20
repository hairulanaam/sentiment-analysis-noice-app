import plotly.express as px
import streamlit as st
from config import DARK_TEXT_COLOR, FONT_FAMILY, POSITIVE_COLOR
from utils.data_loader import compute_top_words

def top_words(df_filtered):
    with st.container(border=True, key="top_words_card_container"):
        st.markdown(
            '<div class="section-header">Top Words</div>',
            unsafe_allow_html=True,
        )

        top_10_df = compute_top_words(df_filtered, n=10)

        if top_10_df is not None:
            fig = px.bar(
                top_10_df,
                x='Frequency',
                y='Word',
                orientation='h',
                text='Frequency',
                color_discrete_sequence=[POSITIVE_COLOR],
            )
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                margin=dict(l=10, r=10, t=10, b=10),
                height=270,
                xaxis=dict(showgrid=False, visible=False),
                yaxis=dict(
                    showgrid=False,
                    title=None,
                    tickfont=dict(
                        size=12,
                        family=FONT_FAMILY,
                        color=DARK_TEXT_COLOR,
                    ),
                ),
            )
            fig.update_traces(
                texttemplate='%{text:,}',
                textposition='inside',
                textfont=dict(size=12, color='white', family=FONT_FAMILY),
                marker=dict(line=dict(width=0)),
            )
            st.plotly_chart(fig, use_container_width=True, key="top_words_chart", config={"displayModeBar": False})
        else:
            st.info("No words found for top 10 frequencies.")
