from __future__ import annotations

from app.people.cinema_staff import Cleaner


class CinemaHall:

    def __init__(self, number: int) -> CinemaHall:
        self.number = number

    def movie_session(self,
                      movie_name: str,
                      customers: list,
                      cleaning_staff: Cleaner) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            print(f'{customer.name} is watching "{movie_name}".')
        print(f'"{movie_name}" ended.')
        print(f"Cleaner {cleaning_staff.name} is cleaning hall number"
              f" {self.number}.")
