from __future__ import annotations

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[Customer],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    viewers = []
    for customer in customers:
        viewers.append(Customer(customer["name"], customer["food"]))
    bar_service = CinemaBar()
    current_hall = CinemaHall(hall_number)
    clean_serve = Cleaner(cleaner)
    for viewer in viewers:
        bar_service.sell_product(viewer, viewer.food)
    current_hall.movie_session(movie, viewers, clean_serve)
