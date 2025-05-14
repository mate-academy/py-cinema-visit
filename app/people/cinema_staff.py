from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.cinema.hall import CinemaHall


class Cleaner:

    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: "CinemaHall.number") -> None:
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
