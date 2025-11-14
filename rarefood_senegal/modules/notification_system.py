# rarefood_senegal/modules/notification_system.py
notifications = []

def get_notifications(email):
    return [n for n in notifications if n["destinataire"] == email]

def mark_as_read(notification_id):
    for n in notifications:
        if n["id"] == notification_id:
            n["lu"] = True

def send_notification(destinataire, message):
    from uuid import uuid4
    notifications.append({
        "id": str(uuid4()),
        "destinataire": destinataire,
        "message": message,
        "date": "aujourd’hui",
        "lu": False
    })
