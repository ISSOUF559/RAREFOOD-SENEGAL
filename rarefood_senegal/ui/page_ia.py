# rarefood_senegal/ui/page_ia.py
import streamlit as st
from rarefood_senegal.modules import agent_ia

def run():
    st.title("Suggestions IA")
    role = st.selectbox("Votre rôle", ["Client", "Producteur", "Admin"])
    suggestions = agent_ia.suggest_for_role(role)
    for s in suggestions:
        st.markdown(f"- 💡 {s}")
