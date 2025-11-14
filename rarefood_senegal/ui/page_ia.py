import streamlit as st
from rarefood_senegal.modules import agent_ia
def run():
    st.title("Suggestions IA")
    role = st.selectbox("Votre rôle", ["Client", "Producteur", "Admin"])
    for s in agent_ia.suggest_for_role(role):
        st.markdown(f"- {s}")