import streamlit as st

st.subheader("⭐ Avis des clients")

avis = [
    {"nom": "Fatou", "produit": "Mangue", "note": 5, "commentaire": "Délicieuse et bien mûre !"},
    {"nom": "Ibrahima", "produit": "Citron", "note": 4, "commentaire": "Très parfumé, parfait pour le jus."},
    {"nom": "Awa", "produit": "Papaye", "note": 5, "commentaire": "Excellente qualité, livraison rapide."}
]

for a in avis:
    st.write(f"👤 {a['nom']} – 🛒 {a['produit']} – ⭐ {a['note']}/5")
    st.markdown(f"_{a['commentaire']}_")
