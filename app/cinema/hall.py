"""
hall.py

This module describes actions during a movie session in a cinema hall.
"""

from typing import List

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    """Represents a cinema hall where movie sessions take place."""

    def __init__(self, number: int) -> None:
        """
        :param number: int, the number of the cinema hall.
        """
        self.number = number

    def movie_session(
        self,
        movie_name: str,
        customers: list[Customer],
        cleaning_staff: Cleaner,
    ) -> None:
        """
        Run a full movie session: announce the start, let customers watch
        the movie, announce the end, and have the cleaner clean the hall.

        :param movie_name: str, the name of the movie being shown.
        :param customers: list of Customer, the customers watching the movie.
        :param cleaning_staff: Cleaner, the cleaner who will clean the hall
            after the session.
        """
        print(f'"{movie_name}" started in hall number {self.number}.')

        for customer in customers:
            customer.watch_movie(movie=movie_name)

        print(f'"{movie_name}" ended.')

        cleaning_staff.clean_hall(hall_number=self.number)
