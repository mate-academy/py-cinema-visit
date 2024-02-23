from typing import List

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
        self,
        movie_name: str,
        customers: List[Customer],
        cleaning_staff: Cleaner
    ) -> None:
        start_message = f'"{movie_name}" started in hall number {self.number}.'
        end_message = f'"{movie_name}" ended.'
        print(start_message)
        for customer in customers:
            customer.watch_movie(movie_name)
        print(end_message)
        cleaning_staff.clean_hall(self.number)
