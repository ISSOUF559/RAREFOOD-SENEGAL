# rarefood_senegal/modules/recommendation_engine.py
def recommend_products(region, saison, stock):
    from rarefood_senegal.modules.product_storage import products
    return [p for p in products if p["categorie"] in saison and p["region"] == region and stock.get(p["nom"], 0) > 0]
