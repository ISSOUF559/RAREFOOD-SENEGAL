import streamlit as st

st.subheader("📊 Tableau de monitoring")

st.metric(label="Commandes en cours", value="42")
st.metric(label="Produits actifs", value="18")
st.metric(label="Utilisateurs connectés", value="7")
st.metric(label="Alertes de sécurité", value="0")

st.line_chart({
    "Commandes": [10, 15, 20, 25, 30, 42],
    "Utilisateurs": [2, 3, 4, 5, 6, 7]
})
