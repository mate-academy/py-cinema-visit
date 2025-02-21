from typing import Callable
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: list, cleaner: Cleaner) -> None:
        print(f"\"{movie_name}\" started in hall number {self.number}.")
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f"\"{movie_name}\" ended.")
        cleaner.clean_hall(self.number)
