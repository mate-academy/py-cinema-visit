from __future__ import annotations

from bleach.sanitizer import Cleaner

from app.bar import Customer


def clean_hall(number: int) -> None:
    pass


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
        self,
        movie_name: str,
        cleaning_staff: Cleaner,
        customers: list[Customer]
    ) -> None:
        print(f"{movie_name} started in hall number {self.number}.")
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)
