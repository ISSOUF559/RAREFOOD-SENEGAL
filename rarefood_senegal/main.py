import streamlit as st
from rarefood_senegal.ui import (
    page_accueil,
    page_commandes,
    page_produits,
    page_clients,
    page_producteurs,
    page_messagerie,
    page_avis,
    page_facturation,
    page_certification,
    page_ia,
    page_monitoring,
    page_notifications,
    page_stock,
    page_securite,
    page_recherche,
    page_galerie,
    page_impact,
    page_admin,
    page_backup,
    page_temoin,
    page_formation,
    page_multilingue,
    page_pilote,
    page_profil,
    page_livraison
)

st.set_page_config(
    page_title="RAREFOOD Sénégal",
    page_icon="🍽️",
    layout="wide"
)

st.sidebar.title("📦 Menu principal")
st.sidebar.markdown("🔐 Sécurité active : CAPTCHA artisanal + journal des échecs")

pages = {
    "🏠 Accueil": page_accueil.run,
    "📦 Commandes": page_commandes.run,
    "🛒 Produits": page_produits.run,
    "👥 Clients": page_clients.run,
    "👨‍🌾 Producteurs": page_producteurs.run,
    "💬 Messagerie": page_messagerie.run,
    "⭐ Avis": page_avis.run,
    "🧾 Facturation": page_facturation.run,
    "🎓 Certification": page_certification.run,
    "🤖 IA & Recommandation": page_ia.run,
    "📊 Monitoring": page_monitoring.run,
    "🔔 Notifications": page_notifications.run,
    "📦 Stock": page_stock.run,
    "🔐 Journal de sécurité": page_securite.run,
    "🔍 Recherche sémantique": page_recherche.run,
    "🖼️ Galerie": page_galerie.run,
    "🌱 Impact local": page_impact.run,
    "🛡️ Administration": page_admin.run,
    "🗂️ Sauvegardes": page_backup.run,
    "📣 Témoignages": page_temoin.run,
    "🎓 Formation": page_formation.run,
    "🌍 Multilingue": page_multilingue.run,
    "🧭 Tableau pilote": page_pilote.run,
    "👤 Profil utilisateur": page_profil.run,
    "🚚 Livraison": page_livraison.run
}

choix = st.sidebar.radio("Choisissez une page :", list(pages.keys()))
pages[choix]()