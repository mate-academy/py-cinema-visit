from __future__ import annotations

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    visitors = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    hall_numb = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for visitor in visitors:
        CinemaBar.sell_product(visitor.food, visitor)
    hall_numb.movie_session(movie, visitors, cleaner)
