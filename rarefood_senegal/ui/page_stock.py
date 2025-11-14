import streamlit as st
from rarefood_senegal.modules import stock_manager
def run():
    st.title("Gestion des stocks")
    for s in stock_manager.get_all_stocks():
        st.markdown(f"- {s['produit']} : {s['quantite']} (seuil : {s['seuil']})")