from __future__ import annotations

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie_name: str) -> None:
    customers = [Customer(**person) for person in customers]
    cleaner = Cleaner(cleaner)

    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()

    for human in customers:
        cinema_bar.sell_product(human.food, human)

    cinema_hall.movie_session(movie_name, customers, cleaner)
