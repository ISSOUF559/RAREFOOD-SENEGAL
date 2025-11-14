import streamlit as st
from rarefood_senegal.modules import product_storage, review_manager
def run():
    st.title("Catalogue des produits")
    produits = product_storage.get_all_products()
    for p in produits:
        st.image(p["photo"], width=150)
        st.markdown(f"**{p['nom']}** — {p['prix']} FCFA — {p['categorie']}")
        if p["certifie"]:
            st.success("✅ Certifié")
        avis = review_manager.get_reviews(p["id"])
        for a in avis:
            st.markdown(f"- {a['note']}/5 : {a['commentaire']}")