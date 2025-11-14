# rarefood_senegal/ui/page_livraison.py
import streamlit as st
from rarefood_senegal.modules import delivery_tracker

def run():
    st.title("Suivi de livraison")
    email = st.text_input("Email client")
    livraisons = delivery_tracker.get_deliveries(email)
    for l in livraisons:
        st.markdown(f"**Commande :** {l['commande_id']}")
        st.markdown(f"**État :** {l['etat']}")
        st.markdown(f"**Itinéraire :** {l['itineraire']}")
