from __future__ import annotations
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list, hall_number: int,
        cleaner: str, movie: str
) -> None:
    customers_class = []
    for customer in customers:
        customers_class.append(Customer(customer["name"], customer["food"]))
    for customer in customers_class:
        CinemaBar.sell_product(customer.food, customer)
    hall = CinemaHall(hall_number)
    hall_cleaner = Cleaner(cleaner)
    hall.movie_session(movie, customers_class, hall_cleaner)
