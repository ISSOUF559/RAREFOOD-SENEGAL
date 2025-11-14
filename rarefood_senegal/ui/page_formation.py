import streamlit as st
from rarefood_senegal.modules import formation_manager
def run():
    st.title("Formation")
    email = st.text_input("Votre email")
    if email:
        modules = formation_manager.get_modules_for_user(email)
        for m in modules:
            if st.button(f"Valider : {m['titre']}"):
                formation_manager.mark_completed(email, m["id"])
                st.success(f"{m['titre']} validé")