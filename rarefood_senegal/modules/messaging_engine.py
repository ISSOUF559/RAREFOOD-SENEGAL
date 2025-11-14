# rarefood_senegal/modules/messaging_engine.py
messages = []

def send_message(expediteur, destinataire, contenu):
    messages.append({"expediteur": expediteur, "destinataire": destinataire, "contenu": contenu})

def get_messages(email):
    return [m for m in messages if m["destinataire"] == email]
