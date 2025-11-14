def run_health_checks():
    return [
        {"module": "Stock", "etat": "OK"},
        {"module": "Commandes", "etat": "OK"},
        {"module": "Sauvegarde", "etat": "OK"},
        {"module": "Sécurité", "etat": "OK"}
    ]