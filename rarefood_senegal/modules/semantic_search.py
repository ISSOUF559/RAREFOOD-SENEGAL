from rarefood_senegal.modules.product_storage import products
def search(query):
    return [p for p in products if query.lower() in p["nom"].lower() or query.lower() in p["categorie"].lower()]