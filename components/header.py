import base64
import os
import streamlit as st
from config import LOGO_FILENAME
from components.try_sentence import sentiment_dialog


def header():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.dirname(current_dir)
        logo_path = os.path.join(project_dir, "static", LOGO_FILENAME)
        with open(logo_path, "rb") as f:
            logo_base64 = base64.b64encode(f.read()).decode('utf-8')
        logo_html = (
            f'<img src="data:image/webp;base64,{logo_base64}" '
            f'style="height: 50px; object-fit: contain;" />'
        )
    except Exception as e:
        logo_html = f'<!-- Error loading logo: {str(e)} -->'

    with st.container(key="header_container"):
        col_left, col_right = st.columns([3, 1])

        with col_left:
            st.markdown(
                '<h2 class="main-title" style="margin: 0; padding: 0;">Sentiment Analysis</h2>',
                unsafe_allow_html=True,
            )

        with col_right:
            col_logo, col_btn = st.columns([1.2, 1])
            with col_logo:
                st.markdown(
                    f"""
                    <div style="display:flex; align-items:center; justify-content:flex-end; height:100%;">
                        {logo_html}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with col_btn:
                if st.button("Test Sentiment", key="try_sentence_btn"):
                    sentiment_dialog()
