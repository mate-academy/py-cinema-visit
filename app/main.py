from __future__ import annotations
from typing import List

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: List[dict],
        hall_number: int,
        cleaner: str,
        movie: str,
) -> None:
    cleaner_instance = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)

    list_of_customers = []

    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        list_of_customers.append(new_customer)
        CinemaBar.sell_product(
            product=new_customer.food,
            customer=new_customer
        )

    cinema_hall.movie_session(movie, list_of_customers, cleaner_instance)
