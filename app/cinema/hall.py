from __future__ import annotations
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    """A class to represent a cinema hall.

    :param number: The number of the cinema hall.
    :type number: int
    """

    def __init__(self, number: int) -> None:
        """Initializes a CinemaHall object.

        :param number: The number of the cinema hall.
        :type number: int
        """
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list[Customer],
            cleaning_staff: Cleaner
    ) -> None:
        """Simulates a movie session in the cinema hall.

        :param movie_name: The name of the movie being shown.
        :type movie_name: str
        :param customers: A list of customers in the hall.
        :type customers: list[Customer]
        :param cleaning_staff: The cleaner assigned to the hall.
        :type cleaning_staff: Cleaner
        """
        print(f'\"{movie_name}\" started in hall number {self.number}.')

        for customer in customers:
            customer.watch_movie(movie_name)

        print(f'\"{movie_name}\" ended.')

        cleaning_staff.clean_hall(self.number)
