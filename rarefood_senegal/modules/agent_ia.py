def suggest_for_role(role):
    if role == "Client":
        return ["Essayez les produits certifiés de votre région", "Commandez avant rupture de stock"]
    elif role == "Producteur":
        return ["Ajoutez une photo claire pour plus de visibilité", "Suivez les modules de formation pour certification"]
    elif role == "Admin":
        return ["Vérifiez les logs de sécurité", "Planifiez une sauvegarde hebdomadaire"]
    return []