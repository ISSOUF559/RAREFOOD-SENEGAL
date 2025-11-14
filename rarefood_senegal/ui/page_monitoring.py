# rarefood_senegal/ui/page_monitoring.py
import streamlit as st
from rarefood_senegal.modules import health_checker

def run():
    st.title("Monitoring système")
    checks = health_checker.run_health_checks()
    for c in checks:
        st.markdown(f"- ✅ {c['module']} : {c['etat']}")
