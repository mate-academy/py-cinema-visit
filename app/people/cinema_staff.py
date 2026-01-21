from __future__ import annotations


class Cleaner:
    """A class to represent a cleaner.

    :param name: The name of the cleaner.
    :type name: str
    """

    def __init__(self, name: str) -> None:
        """Initializes a Cleaner object.

        :param name: The name of the cleaner.
        :type name: str
        """
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        """Cleans a cinema hall.

        :param hall_number: The number of the hall to clean.
        :type hall_number: int
        """
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
