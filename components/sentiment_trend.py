import plotly.graph_objects as go
import streamlit as st
from config import (
    NEGATIVE_COLOR,
    NEUTRAL_COLOR,
    POSITIVE_COLOR,
    BLACK_TEXT_COLOR,
    MUTED_TEXT_COLOR,
)
from utils.data_loader import compute_trend_data

def sentiment_trend(df_filtered, total_responses):
    with st.container(border=True, key="trend_card_container"):
        st.markdown(
            f"""
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
                <div class="section-header" style="margin-bottom:0px;">Sentiment Trend</div>
                <div style="display:flex; align-items:center; gap:16px;">
                    <div style="display:flex; align-items:center; gap:6px;">
                        <div style="width:12px; height:12px; background:{POSITIVE_COLOR}; border-radius:3px;"></div>
                        <span style="font-size:13px; font-weight:600; color: {BLACK_TEXT_COLOR};">Positive</span>
                    </div>
                    <div style="display:flex; align-items:center; gap:6px;">
                        <div style="width:12px; height:12px; background:{NEUTRAL_COLOR}; border-radius:3px;"></div>
                        <span style="font-size:13px; font-weight:600; color: {BLACK_TEXT_COLOR};">Neutral</span>
                    </div>
                    <div style="display:flex; align-items:center; gap:6px;">
                        <div style="width:12px; height:12px; background:{NEGATIVE_COLOR}; border-radius:3px;"></div>
                        <span style="font-size:13px; font-weight:600; color: {BLACK_TEXT_COLOR};">Negative</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if total_responses > 0:
            trend_df = compute_trend_data(df_filtered)

            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=trend_df.index, y=trend_df['positive'],
                name='Positive',
                mode='lines+markers',
                line=dict(color=POSITIVE_COLOR, width=2.5),
                marker=dict(size=6, color=POSITIVE_COLOR),
                hovertemplate='%{x|%b %Y}<br>Positive: %{y}<extra></extra>',
            ))
            fig.add_trace(go.Scatter(
                x=trend_df.index, y=trend_df['neutral'],
                name='Neutral',
                mode='lines+markers',
                line=dict(color=NEUTRAL_COLOR, width=2.5),
                marker=dict(size=6, color=NEUTRAL_COLOR),
                hovertemplate='%{x|%b %Y}<br>Neutral: %{y}<extra></extra>',
            ))
            fig.add_trace(go.Scatter(
                x=trend_df.index, y=trend_df['negative'],
                name='Negative',
                mode='lines+markers',
                line=dict(color=NEGATIVE_COLOR, width=2.5),
                marker=dict(size=6, color=NEGATIVE_COLOR),
                hovertemplate='%{x|%b %Y}<br>Negative: %{y}<extra></extra>',
            ))

            fig.update_layout(
                xaxis=dict(
                    title=None,
                    tickformat="%b %Y",
                    showgrid=False,
                    tickfont=dict(size=11, color=MUTED_TEXT_COLOR),
                    linecolor='rgba(128,128,128,0.2)',
                ),
                yaxis=dict(
                    title=dict(text="Total", font=dict(size=12, color=MUTED_TEXT_COLOR)),
                    showgrid=True,
                    gridcolor='rgba(128,128,128,0.1)',
                    zeroline=True,
                    zerolinecolor='rgba(128,128,128,0.2)',
                    tickfont=dict(size=11, color=MUTED_TEXT_COLOR),
                ),
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                margin=dict(l=10, r=10, t=10, b=10),
                height=370,
                showlegend=False,
                hovermode='x unified',
            )
            st.plotly_chart(fig, use_container_width=True, key="sentiment_line")
        else:
            st.info("No data available for the selected date range.")
