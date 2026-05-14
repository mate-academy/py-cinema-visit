from __future__ import annotations
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie_name: str) -> None:
    cinema_hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaner)
    customers_list = []
    for customer in customers:
        customer_instance = Customer(
            name=customer["name"],
            food=customer["food"])
        customers_list.append(customer_instance)
        CinemaBar.sell_product(
            customer=customer_instance,
            product=customer["food"])
    cinema_hall.movie_session(
        movie_name=movie_name,
        customers=customers_list,
        cleaning_staff=cleaner)
