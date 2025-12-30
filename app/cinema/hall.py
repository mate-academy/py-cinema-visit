from typing import List
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: List[Customer], cleaning_staff: Cleaner) -> None:
        # announce start
        print(f'"{movie_name}" started in hall number {self.number}.')
        # each customer watches movie
        for customer in customers:
            customer.watch_movie(movie_name)
        # announce end
        print(f'"{movie_name}" ended.')
        # cleaner cleans the hall
        cleaning_staff.clean_hall(hall_number=self.number)
