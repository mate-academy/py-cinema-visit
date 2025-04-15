from __future__ import annotations
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_instances_list = [Customer(one["name"], one["food"])
                                for one in customers]
    for one in customers_instances_list:
        CinemaBar.sell_product(one.food, one)
    CinemaHall.movie_session(CinemaHall(hall_number),
                             movie,
                             customers_instances_list,
                             Cleaner(cleaner))
