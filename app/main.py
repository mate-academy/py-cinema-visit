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
    customers_object = []
    for user in customers:
        customer = Customer(user["name"], user["food"])
        customers_object.append(customer)
        CinemaBar.sell_product(customer.food, customer)
    hall = CinemaHall(hall_number)
    staff = Cleaner(cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=customers_object,
        cleaning_staff=staff
    )
