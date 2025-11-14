# rarefood_senegal/ui/page_commandes.py
import streamlit as st
from rarefood_senegal.modules import order_storage, invoice_generator

def run():
    st.title("Commandes")
    email = st.text_input("Votre email")
    panier = st.text_area("Produits commandés")
    if st.button("Valider la commande"):
        commande = order_storage.create_order(email, panier)
        st.success("Commande enregistrée ✅")
        facture = invoice_generator.generate_invoice(commande)
        st.download_button("Télécharger la facture", facture, file_name="facture.pdf")
