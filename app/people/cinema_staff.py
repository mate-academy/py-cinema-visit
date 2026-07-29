"""
cinema_staff.py

This module describes cinema staff members.
"""


class Cleaner:
    """Represents a cleaner who cleans cinema halls."""

    def __init__(self, name: str) -> None:
        """
        :param name: str, the name of the cleaner.
        """
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        """
        Print that the cleaner is cleaning the given hall.

        :param hall_number: int, the number of the hall to clean.
        """
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
