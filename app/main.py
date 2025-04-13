from __future__ import annotations
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:
    instances_of_customers = []
    for customer in customers:
        instance_of_customer = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(instance_of_customer.food, instance_of_customer)
        instances_of_customers.append(instance_of_customer)
    instance_of_session = CinemaHall(hall_number)
    instance_of_cleaner = Cleaner(cleaning_staff)
    instance_of_session.movie_session(
        movie_name,
        instances_of_customers,
        instance_of_cleaner
    )
