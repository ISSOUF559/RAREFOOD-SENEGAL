# rarefood_senegal/modules/certification_manager.py
from rarefood_senegal.modules.product_storage import products

def get_eligible_products():
    return [p for p in products if not p["certifie"]]

def certify_product(produit_id):
    for p in products:
        if p["id"] == produit_id:
            p["certifie"] = True
