from __future__ import annotations

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    customers_instances = [
        Customer(name=person["name"], food=person["food"])
        for person in customers
    ]
    cinema_hall = CinemaHall(number=hall_number)
    cinema_bar = CinemaBar()
    worker_staff = Cleaner(name=cleaner)

    for people in customers_instances:
        cinema_bar.sell_product(people, people.food)

    cinema_hall.movie_session(movie_name=movie,
                              customers=customers_instances,
                              cleaning_staff=worker_staff)
    pass
