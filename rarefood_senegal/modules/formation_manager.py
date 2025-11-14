# rarefood_senegal/modules/formation_manager.py

formations = {
    "producteur": [
        {"id": "F001", "titre": "Hygiène alimentaire", "etat": "non validé"},
        {"id": "F002", "titre": "Traçabilité des produits", "etat": "non validé"},
        {"id": "F003", "titre": "Certification locale", "etat": "non validé"}
    ],
    "client": [
        {"id": "F004", "titre": "Consommation responsable", "etat": "non validé"},
        {"id": "F005", "titre": "Lecture des étiquettes", "etat": "non validé"}
    ]
}

validation = {}

def get_modules_for_role(role):
    return formations.get(role, [])

def get_modules_for_user(email):
    return validation.get(email, get_modules_for_role("client"))

def mark_completed(email, module_id):
    if email not in validation:
        validation[email] = get_modules_for_role("client")
    for m in validation[email]:
        if m["id"] == module_id:
            m["etat"] = "validé"
