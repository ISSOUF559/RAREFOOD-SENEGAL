# rarefood_senegal/ui/page_securite.py
import streamlit as st
from rarefood_senegal.modules import security_manager

def run():
    st.title("Sécurité")
    st.markdown("### Réinitialisation du mot de passe")
    email = st.text_input("Email")
    if st.button("Réinitialiser"):
        code = security_manager.generate_reset_code(email)
        st.success(f"Code envoyé : {code}")

    st.markdown("### Verrouillage automatique")
    tentatives = security_manager.get_failed_attempts(email)
    if tentatives >= 3:
        st.error("Compte verrouillé automatiquement")
