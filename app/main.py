from typing import Any
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: Any,
    hall_number: Any,
    cleaner: Any,
    movie: Any
) -> Any:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    for customer_info in customers:
        customer = Customer(customer_info["name"], customer_info["food"])
        cinema_bar.sell_product(customer, customer.food)

    cinema_hall.movie_session(
        movie,
        [Customer(c["name"], ["food"]) for c in customers],
        cleaning_staff
    )
