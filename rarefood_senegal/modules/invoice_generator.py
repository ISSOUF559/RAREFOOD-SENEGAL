from rarefood_senegal.modules.order_storage import get_orders_by_email
def generate_invoice(commande):
    return f"Facture pour {commande['email']} — Produits : {commande['produits']} — Date : {commande['date']}".encode("utf-8")
def get_orders(email):
    return get_orders_by_email(email)