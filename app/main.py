from __future__ import annotations
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cleaning_staff = Cleaner(cleaner)
    customer_instances = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    for cust in customer_instances:
        CinemaBar.sell_product(cust, cust.food)

    CinemaHall(hall_number).movie_session(movie,
                                          customer_instances,
                                          cleaning_staff)
