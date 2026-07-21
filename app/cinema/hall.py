from typing import TYPE_CHECKING

# The TYPE_CHECKING block is executed only by the analyzer (Pylance),
# but is ignored during actual program execution.
# This solves the problem of circular imports and UndefinedVariable errors.
if TYPE_CHECKING:
    from app.people.cinema_staff import Cleaner


class CinemaHall:
    # Constructor: we save the hall number so that the movie_session method
    # knows where exactly the session is taking place.
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
        self,
        movie_name: str,
        customers: list,
        cleaning_staff: "Cleaner"  # Annotation (Forward Reference)
    ) -> None:
        # 1. Inform about the start of the session, using the hall number from
        # the class attributes
        print(f'"{movie_name}" started in hall number {self.number}.')

        # 2. Iterate through each customer in the provided list
        for customer in customers:
            # 3. Call the 'watch_movie' method on the 'customer' object
            customer.watch_movie(movie_name)

        # 4. Inform about the end of the session
        print(f'"{movie_name}" ended.')

        # 5. Delegate the cleaning task: call the 'clean_hall'
        # method on the 'cleaning_staff' object,
        # passing him the number of the current room.
        cleaning_staff.clean_hall(self.number)
