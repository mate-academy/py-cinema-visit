from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.cinema.hall import CinemaHall


class Cleaner:
    """
    Minimal Cleaner used by tests.
    """
    def __init__(self, name: str) -> None:
        self.name = name

    def clean(self, hall: "CinemaHall") -> None:
        hall.occupied = 0
