# rarefood_senegal/ui/page_messagerie.py
import streamlit as st
from rarefood_senegal.modules import messaging_engine

def run():
    st.title("Messagerie interne")
    email = st.text_input("Votre email")
    destinataire = st.text_input("Destinataire")
    message = st.text_area("Message")
    if st.button("Envoyer"):
        messaging_engine.send_message(email, destinataire, message)
        st.success("Message envoyé ✅")

    st.markdown("### Vos messages reçus")
    messages = messaging_engine.get_messages(email)
    for m in messages:
        st.markdown(f"- 📩 {m['expediteur']} : {m['contenu']}")
