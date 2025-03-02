from typing import List

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    """
    class that describes actions during the movie session.
    """

    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: List["Customer"],
            cleaning_staff: "Cleaner"
    ) -> None:
        """
        This method prints about movie start,
        calls customers method watch_movie,
        prints about movie end, calls cleaner method clean_hall
        """

        print(f'"{movie_name}" started in hall number {self.number}.')

        for customer in customers:
            customer.watch_movie(movie_name)

        print(f'"{movie_name}" ended.')

        cleaning_staff.clean_hall(self.number)
