import streamlit as st

st.subheader("📣 Témoignages des producteurs")

temoins = [
    {"nom": "Amina", "message": "Grâce à RAREFOOD, mes produits atteignent plus de clients chaque semaine."},
    {"nom": "Moussa", "message": "La certification m’a permis d’entrer dans de nouveaux marchés."}
]

for t in temoins:
    st.write(f"👤 {t['nom']} : _{t['message']}_")
