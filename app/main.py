from __future__ import annotations

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    viewers = [
        Customer(viewer["name"], viewer["food"])
        for viewer in customers
    ]

    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)

    for viewer in viewers:
        cinema_bar.sell_product(viewer.food, viewer)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=viewers,
        cleaning_staff=cinema_cleaner
    )
