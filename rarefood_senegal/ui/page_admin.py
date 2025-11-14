import streamlit as st
from rarefood_senegal.modules import user_storage, security_monitor
def run():
    st.title("Espace Administrateur")
    st.markdown("### Utilisateurs enregistrés")
    for u in user_storage.users:
        st.markdown(f"- {u['email']} ({u['role']})")
    st.markdown("### Journal de sécurité")
    for log in security_monitor.get_logs():
        st.markdown(f"- {log['timestamp']} : {log['action']}")