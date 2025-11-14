import random

def generer_question():
    a, b = random.randint(1, 9), random.randint(1, 9)
    return {"a": a, "b": b, "attendu": a + b}

def verifier_reponse(attendu, reponse):
    try:
        return int(reponse) == attendu
    except:
        return False
