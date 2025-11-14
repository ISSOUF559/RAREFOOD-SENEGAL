import streamlit as st
from rarefood_senegal.modules import testimonial_manager
def run():
    st.title("Témoignages producteurs")
    temoins = testimonial_manager.get_all()
    for t in temoins:
        st.markdown(f"**{t['nom']}** ({t['region']}) : {t['message']}")