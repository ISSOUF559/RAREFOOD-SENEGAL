# rarefood_senegal/ui/page_stock.py
import streamlit as st
from rarefood_senegal.modules import stock_manager

def run():
    st.title("Suivi des stocks")
    stocks = stock_manager.get_all_stocks()
    for s in stocks:
        st.markdown(f"**{s['produit']}** — {s['quantite']} unités")
        if s["quantite"] < s["seuil"]:
            st.warning("⚠️ Stock faible")
