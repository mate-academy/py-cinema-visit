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
    customers_list = [
        Customer(
            customer["name"],
            customer["food"]
        ) for customer in customers]

    cleaning_staff = Cleaner(cleaner)

    for customer in customers_list:
        CinemaBar.sell_product(customer.food, customer)

    CinemaHall(hall_number).movie_session(
        movie,
        customers_list,
        cleaning_staff
    )
