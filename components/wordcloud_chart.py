import streamlit as st
from wordcloud import WordCloud

def wordcloud_chart(df_filtered):
    with st.container(border=True, key="wordcloud_card_container"):
        st.markdown(
            '<div class="section-header">Word Cloud</div>',
            unsafe_allow_html=True,
        )

        non_empty_text = df_filtered['text_final'].dropna().astype(str)
        if len(non_empty_text) > 0:
            combined_text = " ".join(non_empty_text)
            if combined_text.strip():
                wc = WordCloud(
                    width=600,
                    height=350,
                    background_color="white",
                    colormap="viridis",
                ).generate(combined_text)
                img = wc.to_image()
                st.image(img, use_container_width=True)
            else:
                st.info("No words available to generate a Word Cloud.")
        else:
            st.info("No preprocessed text data found.")
