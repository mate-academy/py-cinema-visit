from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: List[Dict[str, str]],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    visitors: List[Customer] = []
    for customer in customers:
        visitor = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(visitor.food, visitor)
        visitors.append(visitor)
    CinemaHall(hall_number).movie_session(movie, visitors, Cleaner(cleaner))
