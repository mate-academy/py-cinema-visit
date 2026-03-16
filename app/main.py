from typing import Any
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
    customers: list[Customer],
    hall_number: Any,
    cleaner: Any,
    movie: Any
) -> None:

    customer_list = []

    for customer_data in customers:
        customer = Customer(
            customer_data["name"],
            customer_data["food"]
        )

        CinemaBar.sell_product(
            customer.food,
            customer
        )

        customer_list.append(customer)

    cleaner_staff = Cleaner(cleaner)

    cinema_hall = CinemaHall(hall_number)

    cinema_hall.movie_session(
        movie,
        customer_list,
        cleaner_staff)
