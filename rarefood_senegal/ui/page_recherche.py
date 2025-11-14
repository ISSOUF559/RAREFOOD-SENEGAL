import streamlit as st

st.subheader("🔍 Recherche intelligente")

query = st.text_input("🔎 Que recherchez-vous ? (ex : mangue bio, certification locale)")
if query:
    st.success(f"Résultats pour : {query}")
    st.write("🔎 Mangue bio – Producteur certifié à Ziguinchor")
    st.write("🔎 Certification locale – Formation disponible en ligne")
