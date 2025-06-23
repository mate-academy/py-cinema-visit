import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from app.main import cinema_visit

def test_cinema_visit(capsys):
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    hall_number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"

    cinema_visit(customers=customers, hall_number=hall_number, cleaner=cleaner_name, movie=movie)

    captured = capsys.readouterr()
    expected = '\n'.join([
        "Cinema bar sold Coca-cola to Bob.",
        "Cinema bar sold popcorn to Alex.",
        '"Madagascar" started in hall number 5.',
        'Bob is watching "Madagascar".',
        'Alex is watching "Madagascar".',
        '"Madagascar" ended.',
        'Cleaner Anna is cleaning hall number 5.'
    ])
    assert captured.out.strip() == expected
