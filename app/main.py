from __future__ import annotations

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_cls_list = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    hall = CinemaHall(hall_number)
    staff = Cleaner(cleaner)
    for customer in customers_cls_list:
        CinemaBar.sell_product(customer, customer.food)
    hall.movie_session(movie, customers_cls_list, staff)
