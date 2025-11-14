import streamlit as st
from rarefood_senegal.ui import (
    page_stock,
    page_notifications,
    page_formation,
    page_temoin,
    page_galerie
)

st.subheader("👨‍🌾 Espace producteur")

menu = st.selectbox("📦 Modules producteur :", [
    "📦 Gestion de stock",
    "🔔 Notifications",
    "🎓 Formation",
    "📣 Témoignages",
    "🖼️ Galerie"
])

if menu == "📦 Gestion de stock":
    page_stock.run()
elif menu == "🔔 Notifications":
    page_notifications.run()
elif menu == "🎓 Formation":
    page_formation.run()
elif menu == "📣 Témoignages":
    page_temoin.run()
elif menu == "🖼️ Galerie":
    page_galerie.run()
