from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from typing import List


class CinemaHall:
    def __init__(self, number: int):
        self.hall_number = number
        self.number = number

    def __str__(self):
        return f"Cinema hall {self.hall_number}"



    def movie_session(
        self,
        movie_name: str,
        customers: List[Customer],
        cleaning_staff: Cleaner,
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.hall_number}.')
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.hall_number)

