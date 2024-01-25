from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from typing import List


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str,
                      customers: List[Customer],
                      cleaner: Cleaner) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for cust in customers:
            cust.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        print(f"Cleaner {cleaner.name} is cleaning hall number {self.number}.")
