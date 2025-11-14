import streamlit as st

st.subheader("🛒 Catalogue des produits")

produits = [
    {"nom": "Mangue", "prix": 500, "image": "mangue.jpg"},
    {"nom": "Citron", "prix": 300, "image": "citron.jpg"},
    {"nom": "Gingembre", "prix": 400, "image": "gingembre.jpg"},
    {"nom": "Papaye", "prix": 600, "image": "papaye.jpg"},
    {"nom": "Tomate", "prix": 350, "image": "tomate.jpg"}
]

for p in produits:
    st.image(f"rarefood_senegal/assets/images/{p['image']}", width=150)
    st.write(f"**{p['nom']}** – 💰 {p['prix']} FCFA")
    st.button(f"🧺 Ajouter {p['nom']} au panier")
