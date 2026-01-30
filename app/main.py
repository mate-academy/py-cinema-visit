from __future__ import annotations

from typing import Any

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    movie: Any,
    customers: Any,
    hall_number: Any,
    cleaner: Any,
) -> None:
    if isinstance(movie, list) and isinstance(customers, int):
        movie, customers, hall_number, cleaner = (
            cleaner,
            movie,
            customers,
            hall_number,
        )

    customer_instances = [
        Customer(name=c["name"], food=c["food"])
        for c in customers
    ]

    hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    for cust in customer_instances:
        CinemaBar.sell_product(product=cust.food, customer=cust)

    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaning_staff,
    )
