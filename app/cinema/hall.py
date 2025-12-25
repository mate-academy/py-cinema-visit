from typing import List
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.people.customer import Customer
    from app.people.cinema_staff import Cleaner


class CinemaHall:
    """Class that describes actions during the movie session."""

    def __init__(self, number: int) -> None:
        """
        Initialize cinema hall with its number.

        Args:
            number: number of the hall in the cinema
        """
        self.number = number

    def movie_session(
        self,
        movie_name: str,
        customers: List["Customer"],
        cleaning_staff: "Cleaner"
    ) -> None:
        """
        Conducts a movie session: announces movie start,
        customers watch movie, announces movie end,
        and calls cleaner to clean the hall.

        Args:
            movie_name: name of the movie
            customers: list of Customer instances
            cleaning_staff: Cleaner instance
        """
        # Print about movie start
        print(f""""{movie_name}" started in hall number {self.number}.""")

        # Call customers to watch the movie
        for customer in customers:
            customer.watch_movie(movie_name)

        # Print about movie end
        print(f""""{movie_name}" ended.""")

        # Call cleaner to clean the hall
        cleaning_staff.clean_hall(self.number)
