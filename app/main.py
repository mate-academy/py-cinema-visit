from __future__ import annotations

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customers_in = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    for customer in customers_in:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    hall = CinemaHall(hall_number)
    cl = Cleaner(cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=customers_in,
        cleaning_staff=cl,
    )
