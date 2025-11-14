import streamlit as st
from rarefood_senegal.modules import order_storage, product_storage
import rarefood_senegal.modules.captcha_engine as captcha_engine

def run():
    st.title("Passer une commande")
    email = st.text_input("Votre email")
    produits = product_storage.get_all_products()
    selection = st.multiselect("Produits à commander", [p["nom"] for p in produits])

    if "captcha_cmd" not in st.session_state:
        st.session_state["captcha_cmd"] = captcha_engine.generer_question()
    q = st.session_state["captcha_cmd"]
    reponse = st.text_input(f"Combien font {q['a']} + {q['b']} ?")

    if st.button("Valider la commande"):
        if captcha_engine.verifier_reponse(q["attendu"], reponse):
            order_storage.add_order(email, selection, "aujourd’hui")
            st.success("Commande enregistrée ✅")
            st.session_state["captcha_cmd"] = captcha_engine.generer_question()
        else:
            st.error("CAPTCHA incorrect. Veuillez réessayer.")