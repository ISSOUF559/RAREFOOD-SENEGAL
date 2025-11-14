# rarefood_senegal/ui/page_backup.py
import streamlit as st
from rarefood_senegal.modules import backup_manager

def run():
    st.title("Sauvegarde et restauration")
    if st.button("Sauvegarde manuelle"):
        backup_manager.backup_all_data()
        st.success("Sauvegarde effectuée ✅")

    fichier = st.file_uploader("Fichier de restauration", type=["zip"])
    if fichier and st.button("Restaurer"):
        backup_manager.restore_from_file(fichier)
        st.success("Restauration terminée ✅")
