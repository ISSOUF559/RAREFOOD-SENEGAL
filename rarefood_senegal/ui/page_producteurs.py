import streamlit as st
from rarefood_senegal.modules import product_storage, formation_manager
def run():
    st.title("Espace Producteur")
    email = st.text_input("Email producteur")
    nom = st.text_input("Nom du produit")
    prix = st.number_input("Prix (FCFA)", min_value=100)
    categorie = st.selectbox("Catégorie", ["Fruits", "Légumes", "Céréales", "Épices", "Autres"])
    region = st.selectbox("Région", ["Dakar", "Thiès", "Casamance", "Fouta", "Saloum", "Ziguinchor", "Podor", "Mbour", "Kolda", "Niayes"])
    photo = st.file_uploader("Photo du produit", type=["jpg", "png"])
    if st.button("Ajouter le produit"):
        product_storage.add_product(nom, prix, categorie, email, photo, region)
        st.success("Produit ajouté avec succès ✅")
    st.markdown("### Modules de formation")
    modules = formation_manager.get_modules_for_role("producteur")
    for m in modules:
        st.markdown(f"- {m['titre']} — {m['etat']}")