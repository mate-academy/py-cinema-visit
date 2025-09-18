from typing import List, Optional

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(
        self: "CinemaHall",
        hall_number: Optional[int] = None,
        number: Optional[int] = None,
    ) -> None:
        self.number = hall_number if hall_number is not None else number

    def movie_session(
        self: "CinemaHall",
        movie_name: str,
        customers: List[Customer],
        cleaning_staff: Cleaner,
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(hall_number=self.number)
