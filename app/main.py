from typing import List

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: List[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers_list = []

    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        customers_list.append(customer)
        CinemaBar.sell_product(customer.food, customer)

    cinema = CinemaHall(number=hall_number)
    cleaner = Cleaner(cleaner)
    cinema.movie_session(movie, customers_list, cleaner)
