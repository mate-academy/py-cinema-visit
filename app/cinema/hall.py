from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:

    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_session: str,
            customers: list[Customer],
            cleaning_staff: Cleaner
    ) -> None:
        print(f'"{movie_session}" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie(movie_session)
        print(f'"{movie_session}" ended.')
        cleaning_staff.clean_hall(self.number)
