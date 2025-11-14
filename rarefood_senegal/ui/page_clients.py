# rarefood_senegal/ui/page_clients.py
import streamlit as st
from rarefood_senegal.modules import user_storage, order_storage, review_manager

def run():
    st.title("Espace Client")
    email = st.text_input("Votre email")
    if email:
        profil = user_storage.get_user(email)
        st.markdown(f"**Nom :** {profil.get('nom', 'Inconnu')}")
        commandes = order_storage.get_orders_by_email(email)
        st.markdown("### Vos commandes")
        for c in commandes:
            st.markdown(f"- {c['produits']} — {c['date']}")
            if not review_manager.has_reviewed(email, c["produit_id"]):
                if st.button(f"Laisser un avis pour {c['produits']}", key=c["id"]):
                    st.session_state["avis_produit_id"] = c["produit_id"]
                    st.switch_page("Avis")
