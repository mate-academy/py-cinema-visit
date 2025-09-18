from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.people.customer import Customer
    from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self: 'CinemaHall', number: int = 1, capacity: int = 100) -> None:
        self.number: int = number
        self.capacity: int = capacity

    def movie_session(
        self: 'CinemaHall',
        movie_name: str,
        customers: list['Customer'],
        cleaner: 'Cleaner',
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            print(f'{customer.name} is watching "{movie_name}".')
        print(f'"{movie_name}" ended.')
        cleaner.clean_hall(self.number)
