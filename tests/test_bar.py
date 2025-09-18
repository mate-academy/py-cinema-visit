# tests/test_bar.py

import io
from contextlib import redirect_stdout

from app.people.customer import Customer
from app.cinema.bar import CinemaBar, sell_product   # <-- додали sell_product

def test_cinema_bar_sell_product():
    name = "Alice"
    food = "Sprite"
    customer = Customer(name=name, food=food)
    cb = CinemaBar()
    f = io.StringIO()

    with redirect_stdout(f):
        sell_product(customer=customer, product=customer.food)

    output = f.getvalue().strip()
    assert output == f"Cinema bar sold {food} to {name}."
