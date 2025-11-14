import streamlit as st

st.subheader("👤 Profil utilisateur")

nom = st.text_input("Nom complet")
email = st.text_input("Adresse email")
telephone = st.text_input("Numéro de téléphone")
adresse = st.text_area("Adresse complète")

if st.button("💾 Enregistrer le profil"):
    st.success("✅ Profil enregistré avec succès.")
