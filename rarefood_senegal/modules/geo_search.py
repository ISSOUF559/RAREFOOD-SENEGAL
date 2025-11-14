# rarefood_senegal/modules/geo_search.py
def search_by_region(region):
    from rarefood_senegal.modules.product_storage import products
    return [p for p in products if p.get("region", "") == region]
