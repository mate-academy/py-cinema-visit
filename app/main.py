from __future__ import annotations

from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict], hall_number: int, cleaner: str,
                 movie: str) -> None:
    temp_list = []
    for one_customer in customers:
        temp_customer = Customer(one_customer["name"], one_customer["food"])
        temp_list.append(temp_customer)
        CinemaBar.sell_product(temp_customer, temp_customer.food)
    temp_cinema_hall = CinemaHall(hall_number)
    temp_cleaner = Cleaner(cleaner)
    temp_cinema_hall.movie_session(movie, temp_list, temp_cleaner)
