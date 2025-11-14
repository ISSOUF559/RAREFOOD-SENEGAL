# 🌍 RAREFOOD Sénégal

Plateforme mutualisée pour la valorisation des produits locaux, la traçabilité, la certification, et la réduction du gaspillage alimentaire.

## 🔧 Fonctionnalités principales

- Ajout et certification de produits
- Commandes, facturation PDF, suivi de livraison
- Formation des producteurs avec badges
- Messagerie interne sécurisée par rôle
- IA pour recommandations et analyse territoriale
- Galerie publique, témoignages, impact environnemental
- Multilingue : 🇫🇷 🇬🇧 🇸🇦 🇰🇲
- Tableau de bord pilote et indicateurs institutionnels

## 🧱 Architecture modulaire

- `main.py` : point d’entrée
- `ui/` : interfaces Streamlit par rôle
- `modules/` : logique métier et automatisations
- `assets/` : logo, icônes, photos
- `style_manager.py` : intégration CSS institutionnelle

## 🚀 Déploiement local

```bash
pip install -r requirements.txt
streamlit run rarefood_senegal/main.py
