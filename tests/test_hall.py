import io
from contextlib import redirect_stdout

from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def test_cinema_hall_constructor():
    ch = CinemaHall(6)  # argument pozycyjny, bez nazwanego 'number'
    assert hasattr(ch, "hall_number"), (
        "CinemaHall instance should have 'hall_number' attribute"
    )
    assert ch.hall_number == 6, (
        "Value of attribute 'hall_number' should equal to 6 when "
        "instance is created by 'CinemaHall(6)'"
    )


def test_cinema_hall_movie_session():
    hall = 4
    ch = CinemaHall(hall)  # argument pozycyjny

    customer1_name = "Max"
    food1 = "chips"
    customer1 = Customer(customer1_name, food1)

    customer2_name = "Alex"
    food2 = "popcorn"
    customer2 = Customer(customer2_name, food2)

    movie_name = "I'm Robot"
    cleaner_name = "John"
    cleaner = Cleaner(cleaner_name)

    f = io.StringIO()
    with redirect_stdout(f):
        ch.movie_session(movie_name, [customer1, customer2], cleaner)

    out = f.getvalue()
    expected_output = (
        '"I\'m Robot" started in hall number 4.\n'
        'Max is watching "I\'m Robot".\n'
        'Alex is watching "I\'m Robot".\n'
        '"I\'m Robot" ended.\n'
        'Cleaner John is cleaning hall number 4.\n'
    )

    assert out == expected_output, (
        f"'movie_session' output should equal to:\n{expected_output}\n"
        f"but got:\n{out}"
    )

