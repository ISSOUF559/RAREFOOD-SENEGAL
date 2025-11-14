import streamlit as st
from rarefood_senegal.modules import review_manager, product_storage
import rarefood_senegal.modules.captcha_engine as captcha_engine

def run():
    st.title("Avis clients")
    produits = product_storage.get_all_products()
    produit = st.selectbox("Produit", [p["nom"] for p in produits])
    email = st.text_input("Votre email")
    note = st.slider("Note", 1, 5)
    commentaire = st.text_area("Commentaire")

    if "captcha_avis" not in st.session_state:
        st.session_state["captcha_avis"] = captcha_engine.generer_question()
    q = st.session_state["captcha_avis"]
    reponse = st.text_input(f"Combien font {q['a']} + {q['b']} ?")

    if st.button("Soumettre"):
        pid = [p["id"] for p in produits if p["nom"] == produit][0]
        if captcha_engine.verifier_reponse(q["attendu"], reponse):
            if not review_manager.has_reviewed(email, pid):
                review_manager.add_review(pid, email, note, commentaire)
                st.success("Avis enregistré")
                st.session_state["captcha_avis"] = captcha_engine.generer_question()
            else:
                st.warning("Vous avez déjà évalué ce produit")
        else:
            st.error("CAPTCHA incorrect")