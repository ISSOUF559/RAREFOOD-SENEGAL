# rarefood_senegal/modules/certification_manager.py
def get_eligible_products():
    from rarefood_senegal.modules.product_storage import products
    return [p for p in products if not p["certifie"]]

def certify_product(produit_id):
    from rarefood_senegal.modules.product_storage import products
    for p in products:
        if p["id"] == produit_id:
            p["certifie"] = True
