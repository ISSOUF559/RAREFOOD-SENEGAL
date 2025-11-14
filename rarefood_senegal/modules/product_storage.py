# rarefood_senegal/modules/product_storage.py
import uuid

products = []

def add_product(nom, prix, categorie, email, photo, region):
    produit = {
        "id": str(uuid.uuid4()),
        "nom": nom,
        "prix": prix,
        "categorie": categorie,
        "email": email,
        "photo": photo,
        "certifie": False,
        "region": region
    }
    products.append(produit)

def get_all_products():
    return products

def get_certified_products():
    return [p for p in products if p["certifie"]]


# rarefood_senegal/modules/product_storage.py
#import uuid

products = [
    {
        "id": "P001",
        "nom": "Tomate de Niayes",
        "prix": 300,
        "categorie": "Légumes",
        "email": "producteur1@rarefood.sn",
        "photo": "assets/images/tomate.jpg",
        "certifie": True,
        "region": "Niayes"
    },
    {
        "id": "P002",
        "nom": "Chou de Fouta",
        "prix": 250,
        "categorie": "Légumes",
        "email": "producteur2@rarefood.sn",
        "photo": "assets/images/chou.jpg",
        "certifie": False,
        "region": "Fouta"
    },
    {
        "id": "P003",
        "nom": "Carotte bio de Thiès",
        "prix": 400,
        "categorie": "Légumes",
        "email": "producteur3@rarefood.sn",
        "photo": "assets/images/carotte.jpg",
        "certifie": True,
        "region": "Thiès"
    },
    {
        "id": "P004",
        "nom": "Mangue de Casamance",
        "prix": 600,
        "categorie": "Fruits",
        "email": "producteur4@rarefood.sn",
        "photo": "assets/images/mangue.jpg",
        "certifie": True,
        "region": "Casamance"
    },
    {
        "id": "P005",
        "nom": "Mil du Saloum",
        "prix": 350,
        "categorie": "Céréales",
        "email": "producteur5@rarefood.sn",
        "photo": "assets/images/mil.jpg",
        "certifie": False,
        "region": "Saloum"
    },
    {
        "id": "P006",
        "nom": "Poivron vert de Dakar",
        "prix": 280,
        "categorie": "Légumes",
        "email": "producteur6@rarefood.sn",
        "photo": "assets/images/poivron.jpg",
        "certifie": True,
        "region": "Dakar"
    },
    {
        "id": "P007",
        "nom": "Oignon violet de Podor",
        "prix": 320,
        "categorie": "Légumes",
        "email": "producteur7@rarefood.sn",
        "photo": "assets/images/oignon.jpg",
        "certifie": False,
        "region": "Podor"
    },
    {
        "id": "P008",
        "nom": "Citron de Mbour",
        "prix": 200,
        "categorie": "Fruits",
        "email": "producteur8@rarefood.sn",
        "photo": "assets/images/citron.jpg",
        "certifie": True,
        "region": "Mbour"
    },
    {
        "id": "P009",
        "nom": "Gingembre frais de Kolda",
        "prix": 450,
        "categorie": "Épices",
        "email": "producteur9@rarefood.sn",
        "photo": "assets/images/gingembre.jpg",
        "certifie": False,
        "region": "Kolda"
    },
    {
        "id": "P010",
        "nom": "Papaye de Ziguinchor",
        "prix": 550,
        "categorie": "Fruits",
        "email": "producteur10@rarefood.sn",
        "photo": "assets/images/papaye.jpg",
        "certifie": True,
        "region": "Ziguinchor"
    }
]


def get_certified_products():
    return [p for p in products if p["certifie"]]
