# rarefood_senegal/ui/page_recherche.py
import streamlit as st
from rarefood_senegal.modules import semantic_search, geo_search

def run():
    st.title("Recherche intelligente")
    query = st.text_input("Que recherchez-vous ?")
    if query:
        results = semantic_search.search(query)
        for r in results:
            st.markdown(f"- {r['nom']} — {r['categorie']}")

    st.markdown("### Recherche par terroir")
    region = st.selectbox("Région", ["Dakar", "Thiès", "Casamance", "Fouta", "Autres"])
    terroirs = geo_search.search_by_region(region)
    for t in terroirs:
        st.markdown(f"- {t['produit']} — {t['producteur']}")
