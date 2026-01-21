from __future__ import annotations
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self, movie_name: str,
            customers: list[Customer],
            cleaning_staff: Cleaner
    ) -> None:
        self.movie_start(movie_name, self.number)
        for customer in customers:
            customer.watch_movie(movie_name)
        self.movie_end(movie_name)
        cleaning_staff.clean_hall(self.number)

    @staticmethod
    def movie_start(movie: str, hall_number: int) -> None:
        print(f"\"{movie}\" started in hall number {hall_number}.")

    @staticmethod
    def movie_end(movie: str) -> None:
        print(f"\"{movie}\" ended.")
