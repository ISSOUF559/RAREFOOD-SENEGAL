from datetime import datetime
logs = []
def log_event(action):
    logs.append({"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "action": action})
def get_logs():
    return logs