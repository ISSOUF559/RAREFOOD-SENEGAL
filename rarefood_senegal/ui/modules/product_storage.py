# rarefood_senegal/modules/product_storage.py
import uuid

products = []

def add_product(nom, prix, categorie, email, photo):
    produit = {
        "id": str(uuid.uuid4()),
        "nom": nom,
        "prix": prix,
        "categorie": categorie,
        "email": email,
        "photo": photo,
        "certifie": False
    }
    products.append(produit)

def get_all_products():
    return products

def get_certified_products():
    return [p for p in products if p["certifie"]]
