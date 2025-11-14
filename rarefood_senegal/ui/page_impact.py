# rarefood_senegal/ui/page_impact.py
import streamlit as st
from rarefood_senegal.modules import impact_calculator

def run():
    st.title("Impact environnemental et social")
    impact = impact_calculator.calculate()
    st.metric("CO₂ évité", f"{impact['co2']} kg")
    st.metric("Gaspillage évité", f"{impact['gaspillage']} kg")
    st.metric("Produits valorisés", impact["produits_valorises"])
