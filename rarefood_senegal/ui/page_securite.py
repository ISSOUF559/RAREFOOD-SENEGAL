import streamlit as st
from rarefood_senegal.modules import captcha_log

def run():
    st.title("🔐 Journal de sécurité")
    st.markdown("Voici les tentatives échouées de CAPTCHA enregistrées :")
    st.text(captcha_log.afficher_logs())