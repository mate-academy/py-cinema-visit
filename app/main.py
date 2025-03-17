from __future__ import annotations
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall: int,
        cleaning_staff: str,
        movie_name: str)\
        -> None:
    new_customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    hall_num = CinemaHall(hall)

    cinema_bar = CinemaBar()

    cleaner = Cleaner(cleaning_staff)

    for customer in new_customers:
        cinema_bar.sell_product(customer.food, customer)

    hall_num.movie_session(movie_name, new_customers, cleaner)
