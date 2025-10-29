from typing import Iterable
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: Iterable[Customer], hall_number: int, cleaner: Cleaner, movie: str):
    for customer in customers:
        CinemaBar.sell_product(customer.name, customer.food)
    CinemaHall(hall_number).movie_session(movie, customers, cleaner)
