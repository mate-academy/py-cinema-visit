from typing import List

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: List[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = []
    for customer_dict in customers:
        customer_visitor = Customer(
            customer_dict["name"],
            customer_dict["food"]
        )
        customer_instances.append(customer_visitor)

        CinemaBar.sell_product(
            product=customer_visitor.food,
            customer=customer_visitor
        )
    CinemaHall(hall_number).movie_session(
        movie,
        customer_instances,
        Cleaner(cleaner)
    )
