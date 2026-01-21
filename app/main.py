from __future__ import annotations
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cleaner = Cleaner(cleaner)
    cinema_hall_object = CinemaHall(hall_number)
    customers_list = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    for customer in customers_list:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    cinema_hall_object.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner
    )
