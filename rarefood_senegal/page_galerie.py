# rarefood_senegal/ui/page_galerie.py
import streamlit as st
from rarefood_senegal.modules import product_storage

def run():
    st.title("Galerie des produits certifiés")
    produits = product_storage.get_certified_products()
    for p in produits:
        st.image(p["photo"], width=150)
        st.markdown(f"**{p['nom']}** — {p['region']}")
