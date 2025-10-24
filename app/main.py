from typing import Dict, List

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
    customer_objs: List[Customer] = [
        Customer(name=item["name"], food=item["food"]) for item in customers
    ]

    for customer in customer_objs:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    CinemaHall(number=hall_number).movie_session(
        movie_name=movie,
        customers=customer_objs,
        cleaning_staff=Cleaner(name=cleaner),
    )
