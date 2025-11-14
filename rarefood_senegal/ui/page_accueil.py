# rarefood_senegal/ui/page_accueil.py
import streamlit as st

def run():
    st.title("Bienvenue sur RAREFOOD Sénégal")
    st.markdown("""
    Plateforme mutualisée pour la valorisation des produits locaux, la traçabilité, et la réduction du gaspillage alimentaire.
    """)
    st.image("assets/logo.png", width=150)
    st.markdown("**Innovation :** Intelligence artisanale + Intelligence artificielle")
