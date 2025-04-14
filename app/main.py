from __future__ import annotations
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    hall_cleaner = Cleaner(name=cleaner)

    customers_list = []
    for cust_info in customers:
        customer = Customer(name=cust_info["name"], food=cust_info["food"])
        customers_list.append(customer)
        cinema_bar.sell_product(customer=customer, product=customer.food)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=hall_cleaner,
    )
