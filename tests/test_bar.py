import pytest
import io

from contextlib import redirect_stdout

from app.cinema.bar import CinemaBar
from app.people.customer import Customer


def test_cinema_bar_sell_product():
    name = "Alice"
    food = "Sprite"
    customer = Customer(name=name, food=food)
    cb = CinemaBar()
    f = io.StringIO()

    with redirect_stdout(f):
        cb.sell_product(customer=customer, product=customer.food)

    out = f.getvalue()
    output = "Cinema bar sold Sprite to Alice.\n"
    assert out == output, (
        f"'sell_product' output should equal to {output}, "
        f"when customer's name equals to {name} and customer's food equals to {food}"
    )