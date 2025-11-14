import streamlit as st

st.subheader("🖼️ Galerie des produits")

images = [
    "mangue.jpg", "citron.jpg", "gingembre.jpg", "papaye.jpg", "tomate.jpg"
]

for img in images:
    st.image(f"rarefood_senegal/assets/images/{img}", caption=img.split(".")[0].capitalize(), width=200)
