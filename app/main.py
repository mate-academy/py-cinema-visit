from __future__ import annotations
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cleaning_staff = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    customer_list = []
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        customer_list.append(customer)
    for cust in customer_list:
        CinemaBar.sell_product(cust, cust.food)
    hall.movie_session(movie, customer_list, cleaning_staff)
