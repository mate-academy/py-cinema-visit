from __future__ import annotations
from typing import Iterable

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, hall_number: int) -> None:
        # Armazene apenas hall_number, conforme o spec
        self.hall_number = hall_number

    def movie_session(
        self,
        movie_name: str,
        customers: Iterable[Customer],
        cleaning_staff: Cleaner,
    ) -> None:
        # Chame customer.watch_movie(movie=...)
        for customer in customers:
            customer.watch_movie(movie=movie_name)

        # E depois cleaning_staff.clean_hall(hall_number=...)
        cleaning_staff.clean_hall(hall_number=self.hall_number)
