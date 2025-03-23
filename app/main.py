from typing import Dict

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[Dict[str, str]],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customers_instances = [
        Customer(customer.get("name"), customer.get("food"))
        for customer in customers
    ]
    cinemahall = CinemaHall(hall_number)
    cinemebar = CinemaBar()
    cleaner_instance = Cleaner(cleaner)
    for customer in customers_instances:
        cinemebar.sell_product(customer.food, customer)
    cinemahall.movie_session(movie, customers_instances, cleaner_instance)
