from __future__ import annotations
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    cinema_cleaner = Cleaner(name=cleaner)
    #   cleaner_instance = Cleaner(name=cleaner)

    for customer_info in customers:
        customer = Customer(name=customer_info["name"],
                            food=customer_info["food"])
        cinema_bar.sell_product(customer=customer, product=customer.food)

    cinema_hall.movie_session(movie_name=movie,
                              customers=[Customer(**c) for c in customers],
                              cleaning_staff=cinema_cleaner)
