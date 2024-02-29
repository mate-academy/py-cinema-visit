from __future__ import annotations

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict], hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_insts = []
    hall_instance = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    for customer in customers:
        customers_insts.append(Customer(customer["name"], customer["food"]))
    for customer in customers_insts:
        CinemaBar.sell_product(customer, customer.food)
    hall_instance.movie_session(movie, customers_insts, cleaner_instance)
