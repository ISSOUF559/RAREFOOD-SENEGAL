import streamlit as st
from rarefood_senegal.modules import translation_engine
def run():
    st.title("Traduction multilingue")
    texte = st.text_area("Texte à traduire")
    langue = st.selectbox("Langue", ["fr", "en", "ar", "sw", "km"])
    if st.button("Traduire"):
        st.markdown(translation_engine.translate(texte, langue))