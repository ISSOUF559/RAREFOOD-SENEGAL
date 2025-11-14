# rarefood_senegal/ui/page_facturation.py
import streamlit as st
from rarefood_senegal.modules import invoice_generator

def run():
    st.title("Facturation")
    email = st.text_input("Email client")
    commandes = invoice_generator.get_orders(email)
    for c in commandes:
        st.markdown(f"- {c['produits']} — {c['date']}")
        if st.button(f"Générer facture {c['id']}", key=c["id"]):
            pdf = invoice_generator.generate_invoice(c)
            st.download_button("Télécharger la facture", pdf, file_name=f"facture_{c['id']}.pdf")
