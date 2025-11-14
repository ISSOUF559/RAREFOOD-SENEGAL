# rarefood_senegal/modules/review_manager.py
reviews = []

def add_review(produit_id, email, note, commentaire):
    reviews.append({"produit_id": produit_id, "email": email, "note": note, "commentaire": commentaire})

def get_reviews(produit_id):
    return [r for r in reviews if r["produit_id"] == produit_id]

def has_reviewed(email, produit_id):
    return any(r for r in reviews if r["email"] == email and r["produit_id"] == produit_id)
