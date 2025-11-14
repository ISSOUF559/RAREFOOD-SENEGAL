# rarefood_senegal/ui/page_pilote.py
import streamlit as st
from rarefood_senegal.modules import pilot_dashboard

def run():
    st.title("Phase pilote — Indicateurs")
    stats = pilot_dashboard.get_stats()
    st.metric("Commandes", stats["commandes"])
    st.metric("Produits certifiés", stats["certifies"])
    st.metric("Clients actifs", stats["clients"])
    st.metric("Avis clients", stats["avis"])
    st.metric("Taux de satisfaction", f"{stats['satisfaction']}%")
