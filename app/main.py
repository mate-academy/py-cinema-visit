from __future__ import annotations

from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    cleaning = Cleaner(cleaner)
    customers_list = []
    # How many customers came to the movie
    for person in customers:
        customer = Customer(person["name"], person["food"])
        customers_list.append(customer)
        CinemaBar.sell_product(customer, customer.food)

    CinemaHall(hall_number).movie_session(movie, customers_list, cleaning)
