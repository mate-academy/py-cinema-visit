import re
from snacks import SNACKS, list_snacks, get_snack_price, buy_snack, get_snack_by_index

def test_list_snacks_has_all_entries():
    out = list_snacks().strip().splitlines()
    assert len(out) == len(SNACKS)
    assert re.match(r"^\d+\.\s.+\s-\s\d+\sNIS$", out[0])

def test_get_snack_price_valid():
    some = next(iter(SNACKS.keys()))
    assert get_snack_price(some) == SNACKS[some]

def test_get_snack_price_invalid():
    assert get_snack_price("Snack Inexistente") is None

def test_buy_snack_multiplies():
    assert buy_snack("Pipoca", 3, 20) == 60

def test_get_snack_by_index_valid():
    name0 = list(SNACKS.keys())[0]
    price0 = SNACKS[name0]
    assert get_snack_by_index(1) == (name0, price0)

def test_get_snack_by_index_invalid():
    assert get_snack_by_index(0) is None
    assert get_snack_by_index(999) is None
