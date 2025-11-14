# rarefood_senegal/ui/page_formation.py
import streamlit as st
from rarefood_senegal.modules import formation_manager

def run():
    st.title("Formation")
    email = st.text_input("Email utilisateur")
    modules = formation_manager.get_modules_for_user(email)
    for m in modules:
        st.markdown(f"**{m['titre']}** — {m['etat']}")
        if st.button(f"Valider {m['titre']}", key=m["id"]):
            formation_manager.mark_completed(email, m["id"])
            st.success("Module validé ✅")
