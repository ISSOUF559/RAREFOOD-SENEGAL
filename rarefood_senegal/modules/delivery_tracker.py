livraisons = []
def get_deliveries(email):
    return [l for l in livraisons if l["email"] == email]