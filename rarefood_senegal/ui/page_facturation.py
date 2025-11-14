import streamlit as st

st.subheader("🧾 Facturation")

factures = [
    {"id": "F001", "montant": 3500, "statut": "Payée"},
    {"id": "F002", "montant": 4200, "statut": "En attente"}
]

for f in factures:
    st.write(f"🧾 Facture {f['id']} – 💰 {f['montant']} FCFA – ✅ {f['statut']}")
