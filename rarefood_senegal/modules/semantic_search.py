# rarefood_senegal/modules/semantic_search.py
def search(query):
    from rarefood_senegal.modules.product_storage import products
    return [p for p in products if query.lower() in p["nom"].lower() or query.lower() in p["categorie"].lower()]
