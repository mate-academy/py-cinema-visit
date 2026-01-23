from typing import List, Dict

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: List[Dict[str, str]],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    customer_instances = []
    for customer in customers:
        customer_instances.append(Customer(customer["name"], customer["food"]))
        cinema_bar.sell_product(customer_instances[-1], customer["food"])

    hall.movie_session(movie, customer_instances, cleaner)
