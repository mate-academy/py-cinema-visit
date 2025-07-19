from typing import List, Dict

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
    customers_data: List[Dict[str, str]],
    hall_number: int,
    cleaner_name: str,
    movie_name: str
) -> None:
    hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaner_name)
    cinema_bar = CinemaBar()

    customers = []
    for customer_data in customers_data:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"],
        )
        customers.append(customer)
        cinema_bar.sell_product(customer, customer_data["food"])

    hall.movie_session(
        movie_name,
        customers,
        cleaner,
    )
