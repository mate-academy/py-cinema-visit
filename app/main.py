from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(cleaner)

    customer_instances: List[Customer] = []

    for data in customers:
        customer = Customer(data["name"], data["food"])
        customer_instances.append(customer)

        CinemaBar.sell_product(customer.food, customer)

    hall.movie_session(movie, customer_instances, cleaner_instance)
