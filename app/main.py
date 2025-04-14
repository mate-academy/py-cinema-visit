from __future__ import annotations
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    customers_instances = []

    for customer in customers:
        name, food = customer.values()
        customer_instance = Customer(name, food)
        CinemaBar.sell_product(food, customer_instance)
        customers_instances.append(customer_instance)

    hall.movie_session(movie, customers_instances, cleaner_instance)
