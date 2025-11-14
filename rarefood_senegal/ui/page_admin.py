# rarefood_senegal/ui/page_admin.py
import streamlit as st
from rarefood_senegal.modules import security_monitor, user_storage, pilot_dashboard

def run():
    st.title("Espace Administrateur")
    st.markdown("### Journal de sécurité")
    logs = security_monitor.get_logs()
    for log in logs[-10:]:
        st.markdown(f"- {log['timestamp']} — {log['action']}")

    st.markdown("### Utilisateurs")
    users = user_storage.get_all_users()
    for u in users:
        st.markdown(f"- {u['email']} — {u['role']}")

    st.markdown("### Indicateurs pilote")
    stats = pilot_dashboard.get_stats()
    st.metric("Commandes", stats["commandes"])
    st.metric("Produits certifiés", stats["certifies"])
    st.metric("Clients actifs", stats["clients"])
