import streamlit as st
from rarefood_senegal.modules import user_storage

def run():
    st.title("Modifier mon profil")
    email = st.text_input("Votre email")
    nouveau_role = st.selectbox("Nouveau rôle", ["Client", "Producteur", "Admin"])
    if st.button("Mettre à jour"):
        if user_storage.update_user(email, nouveau_role):
            st.success("Profil mis à jour ✅")
        else:
            st.error("Utilisateur introuvable")