from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:

    def __init__(self, number: int) -> None:
        """
        Initializes a cinema hall.

        Parameters:
        number (int): The hall number.
        """
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list[Customer],
            cleaning_staff: Cleaner
    ) -> None:
        """
        Starts a movie session in the cinema hall.

        Parameters:
        movie_name (str): The name of the movie to be shown.
        customers (list[Customer]): A list of customers watching the movie.
        cleaning_staff (str): The cleaner who will clean the hall
        after the session.
        """
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)
