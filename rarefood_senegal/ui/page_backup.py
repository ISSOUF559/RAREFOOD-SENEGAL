import streamlit as st

st.subheader("🗂️ Sauvegardes et restauration")

st.info("📦 Dernière sauvegarde : 14 novembre 2025 à 18h00")
if st.button("🔄 Lancer une nouvelle sauvegarde"):
    st.success("✅ Sauvegarde lancée avec succès.")
if st.button("♻️ Restaurer la dernière version"):
    st.warning("⚠️ Restauration en cours…")
