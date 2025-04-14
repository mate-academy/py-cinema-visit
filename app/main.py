from __future__ import annotations

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = []

    for customer in customers:
        customer_instance = Customer(
            name=customer["name"], food=customer["food"]
        )
        CinemaBar.sell_product(
            customer=customer_instance, product=customer_instance.food
        )

        customer_instances.append(customer_instance)

    cinema_hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaner)
    cinema_hall.movie_session(
        movie_name=movie, customers=customer_instances, cleaning_staff=cleaner
    )
