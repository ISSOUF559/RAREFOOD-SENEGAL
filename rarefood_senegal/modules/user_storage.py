users = []
def add_user(email, role):
    users.append({"email": email, "role": role})
def get_user(email):
    for u in users:
        if u["email"] == email:
            return u