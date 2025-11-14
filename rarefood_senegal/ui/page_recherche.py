import streamlit as st
from rarefood_senegal.modules import semantic_search, geo_search
def run():
    st.title("Recherche intelligente")
    query = st.text_input("Recherche sémantique")
    if query:
        results = semantic_search.search(query)
        for r in results:
            st.markdown(f"- {r['nom']} ({r['categorie']})")
    region = st.selectbox("Recherche par région", ["Dakar", "Thiès", "Casamance", "Fouta"])
    if region:
        terroirs = geo_search.search_by_region(region)
        for t in terroirs:
            st.markdown(f"- {t['nom']} ({t['categorie']})")