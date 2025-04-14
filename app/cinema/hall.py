"""
hall.py - inside this module create CinemaHall class that describes actions
 during the movie session. Its __init__ method takes and stores number
 - number of the hall in cinema. This class should have only one method
 movie_session, that takes movie_name, customers - list of a customers
 (Customer instances), cleaning_staff - cleaner (Cleaner instance). This
 method prints about movie start, calls customers method watch_movie,
 prints about movie end, calls cleaner method clean_hall.
    # "Madagascar" started in hall number 5.
    # Bob is watching "Madagascar".
    # Alex is watching "Madagascar".
    # "Madagascar" ended.
    # Cleaner Anna is cleaning hall number 5.
"""


from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list[Customer],
            cleaning_staff: Cleaner
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for visitor in customers:
            visitor.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)
