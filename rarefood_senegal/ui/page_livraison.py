import streamlit as st

st.subheader("🚚 Suivi de commande")

commande_id = st.text_input("🔎 Entrez votre numéro de commande")
if commande_id:
    st.success(f"📦 Commande {commande_id} en cours de livraison")
    st.progress(70)
    st.info("🕒 Estimée : livraison dans 2 jours")
