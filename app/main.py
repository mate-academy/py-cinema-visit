from typing import List

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: List[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customer_instances = []

    for customer in customers:
        instance = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(instance.food, instance)
        customer_instances.append(instance)

    session = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    CinemaHall.movie_session(session, movie, customer_instances, cleaner)
