from __future__ import annotations

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie: str,
                      customers: list[Customer],
                      cleaning_staff: Cleaner) -> None:
        print(f'"{movie}" started in hall number {self.number}.')
        for person in customers:
            person.watch_movie(movie)
        print(f'"{movie}" ended.')
        cleaning_staff.clean_hall(self.number)
