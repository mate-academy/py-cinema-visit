from __future__ import annotations
from typing import List

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: List[dict], hall_number: int, cleaner: str, movie: str):
    list_of_customers = []

    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        list_of_customers.append(new_customer)
        CinemaBar.sell_product(new_customer, customer["food"])

    cleaner = Cleaner(cleaner)

    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, list_of_customers, cleaner)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers, hall_number=hall_number, cleaner=cleaner_name, movie=movie)