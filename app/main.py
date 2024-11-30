from typing import List

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: List[Customer],
        hall_number: int,
        cleaner: Cleaner,
        movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    customer_instances = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    for customer in customer_instances:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customer_instances, cleaner)
