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
    customer_objs = [Customer(c["name"], c["food"]) for c in customers]
    for customer in customer_objs:
        CinemaBar.sell_product(customer.food, customer)

    cleaner = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, customer_objs, cleaner)
