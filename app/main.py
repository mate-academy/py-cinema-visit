from __future__ import annotations

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict], hall_number: int,
                 cleaner: str, movie: str) -> None:
    list_of_customers = []

    for customer in customers:
        customer_ = Customer(customer["name"], customer["food"])
        list_of_customers.append(customer_)
        CinemaBar.sell_product(customer["food"], customer_)

    cinema_hall = CinemaHall(hall_number)
    cleaning_stuff = Cleaner(cleaner)
    cinema_hall.movie_session(movie, list_of_customers, cleaning_stuff)
