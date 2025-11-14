import streamlit as st
from rarefood_senegal.modules import delivery_tracker
def run():
    st.title("Suivi des livraisons")
    email = st.text_input("Votre email")
    if email:
        livraisons = delivery_tracker.get_deliveries(email)
        for l in livraisons:
            st.markdown(f"- {l}")