from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    """
    A class representing a cinema hall where movie sessions take place.

    Attributes:
        number (int): The number of the cinema hall.

    Methods:
        movie_session(movie_name: str,
                      customers: list[Customer],
                      cleaning_staff: Cleaner) -> None:

            Manages the movie session, notifies customers,
            and triggers hall cleaning after the movie ends.
    """

    def __init__(self, number: int) -> None:
        """
        Initializes a CinemaHall with the specified number.

        Args:
            number (int): The number of the hall.
        """
        self.number = number

    def movie_session(self, movie_name: str,
                      customers: list[Customer],
                      cleaning_staff: Cleaner) -> None:
        """
        Prints the start and end of the movie, allows customers to watch,
        and triggers hall cleaning.

        Args:
            movie_name (str):
                The name of the movie being shown.
            customers (list[Customer]):
                A list of customers attending the movie.
            cleaning_staff (Cleaner):
                The cleaner responsible for cleaning the hall after the movie.
        """
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie(movie_name)

        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)
