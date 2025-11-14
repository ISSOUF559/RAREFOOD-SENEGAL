# rarefood_senegal/ui/page_certification.py
import streamlit as st
from rarefood_senegal.modules import certification_manager

def run():
    st.title("Certification des produits")
    produits = certification_manager.get_eligible_products()
    for p in produits:
        st.markdown(f"**{p['nom']}** — {p['region']}")
        if st.button(f"Certifier {p['nom']}", key=p["id"]):
            certification_manager.certify_product(p["id"])
            st.success("Produit certifié ✅")
