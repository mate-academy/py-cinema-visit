from __future__ import annotations

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_list = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]

    cinema_bar = CinemaBar()
    hall = CinemaHall(number=hall_number)
    staff = Cleaner(name=cleaner)

    for customer in customer_list:
        cinema_bar.sell_product(product=customer.food,
                                customer=customer)
    hall.movie_session(
        movie_name=movie,
        customers=customer_list,
        cleaning_staff=staff
    )
