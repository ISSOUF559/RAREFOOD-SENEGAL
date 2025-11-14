import streamlit as st
from rarefood_senegal.modules import notification_system
def run():
    st.title("Notifications")
    email = st.text_input("Votre email")
    if email:
        notes = notification_system.get_notifications(email)
        for n in notes:
            st.markdown(f"- {n['date']} : {n['message']}")