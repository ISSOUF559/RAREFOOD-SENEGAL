import datetime

log = []

def enregistrer_echec(page, email):
    log.append({
        "page": page,
        "email": email,
        "timestamp": datetime.datetime.now().isoformat()
    })

def get_logs():
    return log

def afficher_logs():
    if not log:
        return "Aucun échec enregistré."
    return "\n".join([f"[{e['timestamp']}] {e['page']} — {e['email']}" for e in log])