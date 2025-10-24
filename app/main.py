from typing import List, Dict, Final


class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name: Final[str] = name
        self.food: Final[str] = food

    def watch_movie(self, movie: str) -> None:
        print(f'{self.name} is watching "{movie}".')


class Cleaner:
    def __init__(self, name: str) -> None:
        self.name: Final[str] = name

    def clean_hall(self, hall_number: int) -> None:
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")


class CinemaBar:
    @staticme
