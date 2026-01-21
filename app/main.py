from typing import List
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: List[Customer], hall_number: int, cleaner: str, movie: str
) -> None:
    customer_list = []
    for index, value in enumerate(customers):
        customer = Customer(value["name"], value["food"])
        customer_list.append(customer)
        CinemaBar.sell_product(value["food"], customer)
    hall = CinemaHall(hall_number)
    stuff = Cleaner(cleaner)
    hall.movie_session(movie, customer_list, stuff)
