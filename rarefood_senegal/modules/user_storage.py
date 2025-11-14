# rarefood_senegal/modules/user_storage.py
users = []

def get_user(email):
    for u in users:
        if u["email"] == email:
            return u
    return {}

def get_all_users():
    return users

def add_user(email, role):
    users.append({"email": email, "role": role})
