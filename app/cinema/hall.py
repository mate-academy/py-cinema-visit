from __future__ import annotations
from app.people.cinema_staff import Cleaner


class CinemaHall:

    def __init__(self, number: int) -> None:
        self.number = number

    @staticmethod
    def movie_session(
            customers: list,
            hall_number: int,
            cleaning_staff: Cleaner,
            movie_name: str
    ) -> None:
        print(f"{movie_name} starts in hall {hall_number}!")
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f"{movie_name} ended in hall {hall_number}!")
        cleaning_staff.clean_hall(hall_number)
