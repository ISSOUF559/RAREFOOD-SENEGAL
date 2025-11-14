# rarefood_senegal/main.py
import streamlit as st
from rarefood_senegal.ui import (
    page_accueil,
    page_produits,
    page_commandes,
    page_clients,
    page_producteurs,
    page_admin,
    page_notifications,
    page_stock,
    page_securite,
    page_monitoring,
    page_backup,
    page_recherche,
    page_certification,
    page_formation,
    page_ia,
    page_messagerie,
    page_avis,
    page_facturation,
    page_livraison,
    page_pilote,
    page_impact,
    page_galerie,
    page_multilingue,
    page_temoin
)

from rarefood_senegal.ui.style_manager import inject_style

inject_style()
st.set_page_config(page_title="RAREFOOD Sénégal", layout="wide")

menu = st.sidebar.selectbox("📂 Menu", [
    "Accueil", "Produits", "Commandes", "Clients", "Producteurs", "Admin",
    "Notifications", "Stock", "Sécurité", "Monitoring", "Sauvegarde",
    "Recherche", "Certification", "Formation", "IA", "Messagerie", "Avis",
    "Facturation", "Livraison", "Pilote", "Impact", "Galerie", "Multilingue", "Témoignages"
])

pages = {
    "Accueil": page_accueil.run,
    "Produits": page_produits.run,
    "Commandes": page_commandes.run,
    "Clients": page_clients.run,
    "Producteurs": page_producteurs.run,
    "Admin": page_admin.run,
    "Notifications": page_notifications.run,
    "Stock": page_stock.run,
    "Sécurité": page_securite.run,
    "Monitoring": page_monitoring.run,
    "Sauvegarde": page_backup.run,
    "Recherche": page_recherche.run,
    "Certification": page_certification.run,
    "Formation": page_formation.run,
    "IA": page_ia.run,
    "Messagerie": page_messagerie.run,
    "Avis": page_avis.run,
    "Facturation": page_facturation.run,
    "Livraison": page_livraison.run,
    "Pilote": page_pilote.run,
    "Impact": page_impact.run,
    "Galerie": page_galerie.run,
    "Multilingue": page_multilingue.run,
    "Témoignages": page_temoin.run
}

pages[menu]()
