from __future__ import annotations

from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    guest_list = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]

    for customer in guest_list:
        CinemaBar.sell_product(customer, customer.food)

    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, guest_list, Cleaner(cleaner))
