orders = []
def add_order(email, produits, date):
    orders.append({"email": email, "produits": produits, "date": date})
def get_orders_by_email(email):
    return [o for o in orders if o["email"] == email]