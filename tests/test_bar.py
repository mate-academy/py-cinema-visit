import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from app.cinema.bar import CinemaBar
from app.people.customer import Customer

def test_sell_product(capsys):
    customer = Customer(name="Bob", food="popcorn")
    CinemaBar.sell_product(product=customer.food, customer=customer)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Cinema bar sold popcorn to Bob."
