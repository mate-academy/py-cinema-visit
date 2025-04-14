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
    cinema_hall_instance = CinemaHall(hall_number)

    customer_instances = []

    for customer in customers:
        customer_instance = Customer(
            name=customer["name"],
            food=customer["food"]
        )
        customer_instances.append(customer_instance)
        CinemaBar.sell_product(
            customer=customer_instance,
            product=customer_instance.food
        )

    cinema_hall_instance.movie_session(
        movie,
        customer_instances,
        Cleaner(cleaner)
    )
