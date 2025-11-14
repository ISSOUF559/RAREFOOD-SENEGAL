import streamlit as st
from rarefood_senegal.ui import (
    page_produits,
    page_commandes,
    page_avis,
    page_livraison,
    page_ia,
    page_recherche,
    page_profil
)

st.set_page_config(page_title="RAREFOOD Sénégal", page_icon="🍽️", layout="wide")

st.markdown("<h1 style='text-align: center; color: #2E8B57;'>BIENVENUE CHEZ RAREFOOD</h1>", unsafe_allow_html=True)

menu = st.tabs([
    "🛒 Produits",
    "🧺 Panier",
    "⭐ Avis",
    "🚚 Suivi commande",
    "🔍 Recherche",
    "👤 Profil",
    "🔑 Connexion",
    "🆕 Créer un compte",
    "❓ Mot de passe oublié",
    "📍 Adresse",
    "📞 Téléphone"
])

with menu[0]: page_produits.run()
with menu[1]: page_commandes.run()
with menu[2]: page_avis.run()
with menu[3]: page_livraison.run()
with menu[4]: page_recherche.run()
with menu[5]: page_profil.run()
with menu[6]: st.info("🔐 Formulaire de connexion à venir...")
with menu[7]: st.info("🆕 Formulaire d'inscription à venir...")
with menu[8]: st.info("❓ Fonction de récupération à venir...")
with menu[9]: st.info("📍 Ajout d'adresse à venir...")
with menu[10]: st.info("📞 Ajout de numéro à venir...")

st.markdown("""
    <div style='position: fixed; bottom: 20px; right: 20px; background-color: #f0f0f0; padding: 10px; border-radius: 10px; box-shadow: 2px 2px 5px gray;'>
        🤖 <strong>Agent IA</strong><br>
        <em>Posez-moi une question sur les produits, les commandes ou les recommandations !</em>
    </div>
""", unsafe_allow_html=True)
