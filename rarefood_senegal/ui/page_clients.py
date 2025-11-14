import streamlit as st
from rarefood_senegal.ui import (
    page_messagerie,
    page_pilote,
    page_certification,
    page_livraison,
    page_avis
)

st.subheader("👥 Espace client")

menu = st.selectbox("🧭 Modules client :", [
    "💬 Messagerie",
    "🧭 Tableau pilote",
    "🎓 Certification",
    "🚚 Suivi commande",
    "⭐ Avis"
])

if menu == "💬 Messagerie":
    page_messagerie.run()
elif menu == "🧭 Tableau pilote":
    page_pilote.run()
elif menu == "🎓 Certification":
    page_certification.run()
elif menu == "🚚 Suivi commande":
    page_livraison.run()
elif menu == "⭐ Avis":
    page_avis.run()
