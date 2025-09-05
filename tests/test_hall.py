import io

from contextlib import redirect_stdout

from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def test_cinema_hall_constructor():
    ch = CinemaHall(number=6)
    assert hasattr(ch, "number"), (
        "CinemaHall instance should have 'number' attribute"
    )
    assert ch.number == 6, (
        f"Value of attribute 'number' should equal to 6 when "
        f"instance is created by 'CinemaHall(number=6)'"
    )


def test_cinema_hall_movie_session():
    hall = 4
    ch = CinemaHall(hall)
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
    output = '"I\'m Robot" started in hall number 4.\n' \
             'Max is watching "I\'m Robot".\n' \
             'Alex is watching "I\'m Robot".\n' \
             '"I\'m Robot" ended.\n' \
             'Cleaner John is cleaning hall number 4.\n'
    assert out == output, (
        f"'movie_session' output should equal to {output}, "
        f"when hall number is {hall}, there are two customers "
        f"{customer1_name} and {customer2_name} and cleaner's "
        f"name is {cleaner_name}"
    )
