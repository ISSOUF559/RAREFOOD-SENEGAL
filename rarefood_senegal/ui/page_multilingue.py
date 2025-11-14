import streamlit as st

st.subheader("🌍 Interface multilingue")

langue = st.selectbox("Choisissez votre langue :", ["Français", "Anglais", "Wolof", "Comorien"])

if langue == "Français":
    st.success("Interface en français activée.")
elif langue == "Anglais":
    st.success("English interface activated.")
elif langue == "Wolof":
    st.success("Jàmm rekk! Interface Wolof activée.")
elif langue == "Comorien":
    st.success("Karibu! Interface Comorienne activée.")
