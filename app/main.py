from __future__ import annotations

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    viewers = [Customer(elem["name"], elem["food"])
               for elem in customers]
    for viewer in viewers:
        CinemaBar.sell_product(viewer.food, viewer)

    current_cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(
        movie, viewers, current_cleaner
    )
