from __future__ import annotations

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    # write you code here
    obj_customers = list()

    for elem in customers:
        customer = Customer(elem["name"], elem["food"])
        obj_customers.append(customer)
        CinemaBar().sell_product(customer, customer.food)

    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, obj_customers, Cleaner(cleaner))


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]

hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"

cinema_visit(customers=customers,
             hall_number=5,
             cleaner="Anna",
             movie="Madagascar")
