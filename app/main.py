from __future__ import annotations

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner_name: str,
                 movie: str) -> None:
    # write you code here
    customer_list = []
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        customer_list.append(new_customer)
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner_name)

    for customer in customer_list:
        CinemaBar.sell_product(customer=customer, product=customer.food)
    cinema_hall.movie_session(movie, customer_list, cleaner)
