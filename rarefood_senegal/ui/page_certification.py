import streamlit as st
from rarefood_senegal.modules import certification_manager
def run():
    st.title("Certification des produits")
    produits = certification_manager.get_eligible_products()
    for p in produits:
        if st.button(f"Certifier {p['nom']}"):
            certification_manager.certify_product(p["id"])
            st.success(f"{p['nom']} certifié")