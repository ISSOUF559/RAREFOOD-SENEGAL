import streamlit as st
from rarefood_senegal.modules import invoice_generator
def run():
    st.title("Facturation")
    email = st.text_input("Email client")
    if email:
        commandes = invoice_generator.get_orders(email)
        for c in commandes:
            if st.button(f"Générer facture : {c['date']}"):
                pdf = invoice_generator.generate_invoice(c)
                st.download_button("Télécharger la facture", pdf, file_name="facture.pdf")