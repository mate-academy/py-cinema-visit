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
    hall = CinemaHall(hall_number)
    staff = Cleaner(cleaner)

    customers_list = []
    for client in customers:
        new_customer = Customer(client["name"], client["food"])
        customers_list.append(new_customer)
        CinemaBar.sell_product(new_customer, new_customer.food)

    hall.movie_session(movie, customers_list, staff)
