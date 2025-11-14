import streamlit as st

st.subheader("💬 Messagerie")

message = st.text_area("✍️ Écrire un message au producteur")
if st.button("📤 Envoyer"):
    st.success("✅ Message envoyé avec succès.")
