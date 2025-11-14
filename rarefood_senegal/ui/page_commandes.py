import streamlit as st

if "panier" not in st.session_state:
    st.session_state.panier = []

produits = [
    {"nom": "Mangue", "prix": 500},
    {"nom": "Citron", "prix": 300},
    {"nom": "Gingembre", "prix": 400},
    {"nom": "Papaye", "prix": 600},
    {"nom": "Tomate", "prix": 350}
]

st.subheader("🛒 Ajouter des produits au panier")
for produit in produits:
    if st.button(f"Ajouter {produit['nom']} ({produit['prix']} FCFA)"):
        st.session_state.panier.append(produit)

st.subheader("🧺 Votre panier")
if st.session_state.panier:
    total = sum(p["prix"] for p in st.session_state.panier)
    for p in st.session_state.panier:
        st.write(f"- {p['nom']} ({p['prix']} FCFA)")
    st.success(f"💰 Total : {total} FCFA")
    if st.button("🗑️ Vider le panier"):
        st.session_state.panier = []
else:
    st.info("Votre panier est vide.")
