from __future__ import annotations

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[Customer],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_list = []
    for customer_dict in customers:
        customers_list.append(Customer(customer_dict["name"],
                                       customer_dict["food"]))

    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cinemas_clean = Cleaner(cleaner)

    for customer in customers_list:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customers_list, cinemas_clean)
