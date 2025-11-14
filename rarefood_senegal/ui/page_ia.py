import streamlit as st

st.subheader("🤖 Agent IA – Recommandation intelligente")

besoin = st.text_input("🧠 Décrivez votre besoin (ex : fruit pour jus, produit longue conservation)")
if besoin:
    st.success("✅ Recommandation IA :")
    if "jus" in besoin.lower():
        st.write("🍍 Papaye – riche en jus, très sucrée")
        st.write("🍋 Citron – parfait pour les boissons fraîches")
    elif "conservation" in besoin.lower():
        st.write("🌾 Mil – longue durée de vie, idéal pour stockage")
        st.write("🥕 Carotte – se conserve plusieurs jours sans réfrigération")
    else:
        st.write("🛒 Mangue – produit phare de la saison")
