from __future__ import annotations

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[Customer],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    list_of_customers = []
    for person in customers:
        customer = Customer(person["name"], person["food"])
        list_of_customers.append(customer)
        CinemaBar.sell_product(person["food"], customer)
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinema_hall.movie_session(movie, list_of_customers, cleaner)
