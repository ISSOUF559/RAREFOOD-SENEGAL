import streamlit as st

st.subheader("🔐 Journal de sécurité")

logs = [
    {"date": "2025-11-14", "action": "Connexion réussie", "utilisateur": "admin"},
    {"date": "2025-11-14", "action": "Échec CAPTCHA", "utilisateur": "client"},
    {"date": "2025-11-13", "action": "Modification profil", "utilisateur": "producteur"}
]

for log in logs:
    st.write(f"📅 {log['date']} – 👤 {log['utilisateur']} – 🛡️ {log['action']}")
