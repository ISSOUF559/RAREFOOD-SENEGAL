# rarefood_senegal/ui/page_multilingue.py
import streamlit as st
from rarefood_senegal.modules import translation_engine

def run():
    st.title("Accessibilité multilingue")
    texte = st.text_area("Texte à traduire")
    langue = st.selectbox("Langue cible", ["Français", "Anglais", "Arabe", "Comorien"])
    if st.button("Traduire"):
        traduction = translation_engine.translate(texte, langue)
        st.success(traduction)
