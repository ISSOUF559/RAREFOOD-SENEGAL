import streamlit as st
from rarefood_senegal.ui import (
    page_monitoring,
    page_backup,
    page_securite,
    page_certification,
    page_facturation,
    page_multilingue
)

st.subheader("🛡️ Interface administrateur")

menu = st.selectbox("📂 Modules admin :", [
    "📊 Monitoring",
    "🗂️ Sauvegardes",
    "🔐 Sécurité",
    "🎓 Certification",
    "🧾 Facturation",
    "🌍 Multilingue"
])

if menu == "📊 Monitoring":
    page_monitoring.run()
elif menu == "🗂️ Sauvegardes":
    page_backup.run()
elif menu == "🔐 Sécurité":
    page_securite.run()
elif menu == "🎓 Certification":
    page_certification.run()
elif menu == "🧾 Facturation":
    page_facturation.run()
elif menu == "🌍 Multilingue":
    page_multilingue.run()
