# rarefood_senegal/ui/page_notifications.py
import streamlit as st
from rarefood_senegal.modules import notification_system

def run():
    st.title("Notifications")
    email = st.text_input("Votre email")
    if email:
        notifs = notification_system.get_notifications(email)
        for n in notifs:
            st.info(f"{n['date']} — {n['message']}")
            notification_system.mark_as_read(n["id"])
