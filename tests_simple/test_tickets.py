from tickets import buy_ticket

def test_buy_ticket_multiplies():
    assert buy_ticket("Qualquer", 2, 45) == 90
    assert buy_ticket("Qualquer", 1, 30) == 30
    assert buy_ticket("Qualquer", 0, 50) == 0
