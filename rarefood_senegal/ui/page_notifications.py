import streamlit as st

st.subheader("🔔 Notifications reçues")

notifications = [
    "📦 Nouvelle commande à préparer",
    "🎓 Formation disponible : Certification locale",
    "🧾 Facture validée par le client"
]

for note in notifications:
    st.success(note)
