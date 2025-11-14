import streamlit as st
from rarefood_senegal.modules import pilot_dashboard
def run():
    st.title("Tableau de bord pilote")
    stats = pilot_dashboard.get_stats()
    for k, v in stats.items():
        st.metric(k.capitalize(), v)