from rarefood_senegal.modules import captcha_engine

def test_captcha_engine():
    q = captcha_engine.generer_question()
    assert isinstance(q, dict)
    assert "a" in q and "b" in q and "attendu" in q
    assert captcha_engine.verifier_reponse(q["attendu"], str(q["attendu"])) == True
    assert captcha_engine.verifier_reponse(q["attendu"], "999") == False
    print("✅ captcha_engine fonctionne correctement")

test_captcha_engine()