from __future__ import annotations
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner_name: str,
                 movie: str) -> None:
    customers_instance = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner_name)
    cinema_bar = CinemaBar()

    for customer in customers_instance:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customers_instance, cleaner)
