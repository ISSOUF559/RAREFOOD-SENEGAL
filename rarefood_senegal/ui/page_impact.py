import streamlit as st
from rarefood_senegal.modules import impact_calculator
def run():
    st.title("Impact environnemental")
    impact = impact_calculator.calculate()
    for k, v in impact.items():
        st.markdown(f"- {k} : {v}")