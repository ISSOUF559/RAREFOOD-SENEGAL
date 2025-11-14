# rarefood_senegal/modules/stock_manager.py
stocks = []

def get_all_stocks():
    return stocks

def update_stock(produit, quantite):
    for s in stocks:
        if s["produit"] == produit:
            s["quantite"] = quantite

def add_stock(produit, quantite, seuil):
    stocks.append({"produit": produit, "quantite": quantite, "seuil": seuil})
