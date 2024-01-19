# main.py
from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: List[Dict[str, str]],
                 hall_number: int, cleaner: str, movie: str) -> None:
    cb = CinemaBar()
    ch = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    customers_instances = [Customer(c["name"], c["food"]) for c in customers]

    for customer in customers_instances:
        cb.sell_product(customer.food, customer)

    ch.movie_session(movie, customers_instances, cleaner)
