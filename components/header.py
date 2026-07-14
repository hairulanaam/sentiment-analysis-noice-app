import base64
import os
import streamlit as st
from config import LOGO_FILENAME

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

    st.markdown(
        f"""
        <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; margin-bottom: 20px;">
            <h2 class="main-title" style="margin: 0; padding: 0;">Sentiment Analysis</h2>
            {logo_html}
        </div>
        """,
        unsafe_allow_html=True
    )
