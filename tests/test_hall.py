import io

from contextlib import redirect_stdout

from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def test_cinema_hall_constructor():
    ch = CinemaHall(hall_number=6)
    assert hasattr(ch, "hall_number"), (
        "CinemaHall instance should have 'hall_number' attribute"
    )
    assert ch.hall_number == 6, (
        f"Value of attribute 'hall_number' should equal to 6 when "
        f"instance is created by 'CinemaHall(hall_number=6)'"
    )


def test_cinema_hall_movie_session():
    hall_value = 4  # Змінено назву змінної для уникнення плутанини
    ch = CinemaHall(hall_number=hall_value)  # ВИПРАВЛЕНО: передаємо hall_number як іменований аргумент

    customer1_name = "Max"
    food1 = "chips"
    customer1 = Customer(name=customer1_name, food=food1)  # ВИПРАВЛЕНО: використовуємо іменовані аргументи

    customer2_name = "Alex"
    food2 = "popcorn"
    customer2 = Customer(name=customer2_name, food=food2)  # ВИПРАВЛЕНО: використовуємо іменовані аргументи

    movie_name = "I'm Robot"
    cleaner_name = "John"
    cleaner = Cleaner(name=cleaner_name)  # ВИПРАВЛЕНО: використовуємо іменований аргумент
    f = io.StringIO()

    with redirect_stdout(f):
        ch.movie_session(movie_name, [customer1, customer2], cleaner)

    out = f.getvalue()
    output = (
        f'"I\'m Robot" started in hall number {hall_value}.\n'  # Використовуємо f-рядок для hall_value
        f'Max is watching "I\'m Robot".\n'
        f'Alex is watching "I\'m Robot".\n'
        f'"I\'m Robot" ended.\n'
        f'Cleaner John is cleaning hall number {hall_value}.\n'  # Використовуємо f-рядок для hall_value
    )
    assert out == output, (
        f"'movie_session' output should equal to {output}, "
        f"when hall number is {hall_value}, there are two customers "
        f"{customer1_name} and {customer2_name} and cleaner's "
        f"name is {cleaner_name}"
    )
