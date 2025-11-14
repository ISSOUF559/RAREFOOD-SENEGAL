import streamlit as st
from rarefood_senegal.modules import messaging_engine
import rarefood_senegal.modules.captcha_engine as captcha_engine

def run():
    st.title("Messagerie interne")
    expediteur = st.text_input("Expéditeur")
    destinataire = st.text_input("Destinataire")
    contenu = st.text_area("Message")

    if "captcha_msg" not in st.session_state:
        st.session_state["captcha_msg"] = captcha_engine.generer_question()
    q = st.session_state["captcha_msg"]
    reponse = st.text_input(f"Combien font {q['a']} + {q['b']} ?")

    if st.button("Envoyer"):
        if captcha_engine.verifier_reponse(q["attendu"], reponse):
            messaging_engine.send_message(expediteur, destinataire, contenu)
            st.success("Message envoyé")
            st.session_state["captcha_msg"] = captcha_engine.generer_question()
        else:
            st.error("CAPTCHA incorrect")

    st.markdown("### Messages reçus")
    messages = messaging_engine.get_messages(destinataire)
    for m in messages:
        st.markdown(f"- {m['expediteur']} : {m['contenu']}")