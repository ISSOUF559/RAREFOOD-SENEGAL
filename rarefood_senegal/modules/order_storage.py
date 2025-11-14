# rarefood_senegal/modules/order_storage.py
import uuid
from datetime import datetime

orders = []

def create_order(email, produits):
    commande = {
        "id": str(uuid.uuid4()),
        "email": email,
        "produits": produits,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "etat": "validée"
    }
    orders.append(commande)
    return commande

def get_orders_by_email(email):
    return [o for o in orders if o["email"] == email]
