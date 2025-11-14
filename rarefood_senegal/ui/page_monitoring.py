import streamlit as st
from rarefood_senegal.modules import health_checker
def run():
    st.title("Monitoring système")
    for check in health_checker.run_health_checks():
        st.markdown(f"- {check['module']} : {check['etat']}")