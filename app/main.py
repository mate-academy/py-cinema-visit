from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from typing import Dict, List


def cinema_visit(
        customers: List[Dict[str, str]],
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:

    customer_instances = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaning_staff)

    for customer in customer_instances:
        CinemaBar.sell_product(customer, customer.food)

    cinema_hall.movie_session(
        movie_name,
        customer_instances,
        cleaner
    )
