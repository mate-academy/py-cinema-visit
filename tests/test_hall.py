import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

def test_movie_session(capsys):
    hall = CinemaHall(hall_number=5)
    customers = [
        Customer(name="Bob", food="Coca-cola"),
        Customer(name="Alex", food="popcorn"),
    ]
    cleaner = Cleaner(name="Anna")
    hall.movie_session(movie_name="Madagascar", customers=customers, cleaning_staff=cleaner)

    captured = capsys.readouterr()
    expected = '\n'.join([
        '"Madagascar" started in hall number 5.',
        'Bob is watching "Madagascar".',
        'Alex is watching "Madagascar".',
        '"Madagascar" ended.',
        'Cleaner Anna is cleaning hall number 5.'
    ])
    assert captured.out.strip() == expected

