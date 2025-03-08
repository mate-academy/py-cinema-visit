from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list[Customer],
            cleaning_stuff: Cleaner
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for visitor in customers:
            visitor.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_stuff.clean_hall(self.number)
