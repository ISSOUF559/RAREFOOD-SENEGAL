# rarefood_senegal/ui/page_avis.py
import streamlit as st
from rarefood_senegal.modules import review_manager

def run():
    st.title("Avis client")
    produit_id = st.session_state.get("avis_produit_id")
    email = st.text_input("Votre email")
    note = st.slider("Note", 1, 5)
    commentaire = st.text_area("Votre avis")
    if st.button("Soumettre l’avis"):
        review_manager.add_review(produit_id, email, note, commentaire)
        st.success("Avis enregistré ✅")
