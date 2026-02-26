from typing import List
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def start_movie(self, movie_name: str) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')

    def end_movie(self, movie_name: str) -> None:
        print(f'"{movie_name}" ended.')

    def movie_session(
        self,
        movie_name: str,
        customers: List[Customer],
        cleaning_staff: Cleaner,
    ) -> None:
        self.start_movie(movie_name)

        for customer in customers:
            customer.watch_movie(movie_name)

        self.end_movie(movie_name)

        cleaning_staff.clean_hall(self.number)
