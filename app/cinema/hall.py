from typing import List

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    """
    Represents a cinema hall in a movie theater.

    The `CinemaHall` class is used to manage
    operations related to a specific hall
    in a cinema, including hosting movie
    sessions and ensuring proper  cleanup after
    the sessions.

    """
    def __init__(self, number: int) -> None:
        """
        Initializes a class instance with the given number.

        This class constructor takes an integer variable
        `number` and stores it as an instance attribute
        to represent specific data associated with the object.

        :param number: An integer value to initialize
            the instance with.
        :type number: int
        """
        self.number = number

    def movie_session(self,
                      movie_name: str,
                      customers: List[Customer],
                      cleaning_staff: Cleaner) -> None:
        """
        Start and manage a movie session in a specific hall.
        The method initiates a movie session with the given name,
        simulates customers watching the movie, and handles
        cleaning operations post-session by the assigned
        cleaning staff.

        :param movie_name: Name of the movie being screened.
        :type movie_name: str
        :param customers: List of Customer objects representing
            individuals watching the movie.
        :type customers: List[Customer]
        :param cleaning_staff: Cleaner object responsible for cleaning
            the hall after the session.
        :type cleaning_staff: Cleaner
        :return: None
        """
        print(f'"{movie_name}" started in hall number {self.number}.')

        for customer in customers:
            customer.watch_movie(movie_name)

        print(f'"{movie_name}" ended.')

        cleaning_staff.clean_hall(self.number)
