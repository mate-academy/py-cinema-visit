from typing import List
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number: int = None, hall_number: int = None) -> None:
        if number is not None:
            self.number = number
            self.hall_number = number
        elif hall_number is not None:
            self.hall_number = hall_number
            self.number = hall_number
        else:
            raise ValueError("Either 'number' or "
                             "'hall_number' must be provided")

    def movie_session(self, movie_name: str,
                      customers: List[Customer],
                      cleaning_staff: Cleaner) -> None:
        print(f'"{movie_name}" started in hall number {self.hall_number}.')
        for customer in customers:
            customer.watch_movie(movie=movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(hall_number=self.hall_number)
