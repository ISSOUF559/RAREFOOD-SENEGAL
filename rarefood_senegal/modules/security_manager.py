# rarefood_senegal/modules/security_manager.py
from random import randint

failed_attempts = {}

def generate_reset_code(email):
    return str(randint(100000, 999999))

def get_failed_attempts(email):
    return failed_attempts.get(email, 0)

def increment_failed_attempts(email):
    failed_attempts[email] = get_failed_attempts(email) + 1
