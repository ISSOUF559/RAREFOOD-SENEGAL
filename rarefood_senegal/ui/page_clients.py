import streamlit as st
from rarefood_senegal.modules import user_storage, order_storage
def run():
    st.title("Espace Client")
    email = st.text_input("Votre email")
    if email:
        user = user_storage.get_user(email)
        if user:
            st.markdown(f"Bienvenue {email} — rôle : {user['role']}")
            commandes = order_storage.get_orders_by_email(email)
            for c in commandes:
                st.markdown(f"- {c['date']} : {c['produits']}")
        else:
            st.warning("Utilisateur inconnu")