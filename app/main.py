from __future__ import annotations
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str)\
        -> None:
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)
    customers_objects = []

    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        cinema_bar.sell_product(customer.food, customer)
        customers_objects.append(customer)
    cinema_hall.movie_session(movie, customers_objects, cleaner)
