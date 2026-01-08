from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    """
    Represents a specific cinema hall and manages the flow of a movie session.

    It coordinates the start of the movie, customer interactions,
    and the subsequent cleaning of the hall.

    Args:
        number (int): The hall number.
    """

    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str,
                      customers: list[Customer],
                      cleaning_staff: Cleaner) -> None:
        """
        Execute a full movie session in chronological order.
            The sequence includes:
                1. Starting the movie session.
                2. Allowing all customers to watch the movie.
                3. Ending the movie session.
                4. Initiating the hall cleaning process.

        Args:
            movie_name (str): The title of the movie being shown.
            customers (list[Customer]): A list of customer
                                        instances in the hall.
            cleaning_staff (Cleaner): The staff member
                                        responsible for cleaning.
        """
        print(f'"{movie_name}" movie session started.')

        for customer in customers:
            customer.watch_movie(movie_name)

        print(f'"{movie_name}" movie session ended.')

        cleaning_staff.clean_hall(self.number)
