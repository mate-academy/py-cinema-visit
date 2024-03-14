from typing import List
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: List[Customer],
            cleaning_staff: Cleaner
    ) -> None:
        """
        A method for conducting a session in a movie theater.

        Parameters:
        - movie_name: str, the name of the movie.
        - customers: List[Customer],
        a list of instances of the Customer class,
        customers who are watching the movie.
        - cleaning_staff: Cleaner,
        an instance of the Cleaner class, the cleaner.

        Returns:
        None
        """
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie(movie=movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(hall_number=self.number)
