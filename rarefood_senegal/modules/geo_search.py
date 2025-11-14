from rarefood_senegal.modules.product_storage import products
def search_by_region(region):
    return [p for p in products if p.get("region", "") == region]