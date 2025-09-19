from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.people.customer import Customer
    from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(
        self,
        hall_number: int | None = None,
        number: int | None = None,
    ) -> None:
        # przyjmij oba warianty i ustaw DWIE nazwy atrybutów
        value = hall_number if hall_number is not None else number
        self.hall_number = value
        self.number = value  # <-- dodane, żeby test hasattr(ch, "number") przechodził

    def movie_session(
        self,
        movie_name: str,
        customers: list["Customer"],
        cleaning_staff: "Cleaner",
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.hall_number}.')
        for customer in customers:
            customer.watch_movie(movie=movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.hall_number)
