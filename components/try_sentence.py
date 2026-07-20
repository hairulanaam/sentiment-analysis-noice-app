import os
import joblib
import streamlit as st

@st.cache_resource
def load_model():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(current_dir)
    model_path = os.path.join(project_dir, "models", "logistic_regression.joblib")
    vectorizer_path = os.path.join(project_dir, "models", "tfidf_vectorizer.joblib")
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    return model, vectorizer


def predict_sentiment(text: str) -> str:
    model, vectorizer = load_model()
    text_vectorized = vectorizer.transform([text])
    prediction = model.predict(text_vectorized)[0]
    return prediction.capitalize()

@st.dialog("Input sentence", width="small")
def sentiment_dialog():
    if "sentiment_result" not in st.session_state:
        st.session_state.sentiment_result = None

    col_input, col_btn = st.columns([3, 1])
    with col_input:
        sentence = st.text_input(
            "Enter a sentence",
            placeholder="Tampilan aplikasi bagus dan mudah digunakan",
            label_visibility="collapsed",
            key="sentiment_input",
        )

    btn_slot = col_btn.empty()
    search_clicked = btn_slot.button("Test", key="search_btn")
    if search_clicked:
        if sentence.strip():
            btn_slot.empty()
            with col_btn:
                with st.spinner(""):
                    result = predict_sentiment(sentence.strip())
            st.session_state.sentiment_result = result
            btn_slot.button("Test", key="search_btn_done")
        else:
            st.warning("Please enter a sentence to analyze.")

    if st.session_state.sentiment_result is not None:
        st.write(f"The sentiment of the sentence is **{st.session_state.sentiment_result.upper()}**")
