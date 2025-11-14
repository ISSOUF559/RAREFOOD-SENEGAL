import streamlit as st
from rarefood_senegal.modules import backup_manager
def run():
    st.title("Sauvegarde")
    if st.button("Sauvegarder"):
        backup_manager.backup_all_data()
        st.success("Sauvegarde effectuée")