from __future__ import annotations
from typing import List


from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: List[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    visitors = [Customer(cust["name"], cust["food"]) for cust in customers]
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    for customer in visitors:
        cinema_bar.sell_product(customer, customer.food)
    cinema_hall.movie_session(movie, visitors, cleaning_staff)
