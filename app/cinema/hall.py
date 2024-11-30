from app.people import Cleaner
from app.people import Customer


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list,
            cleaning_staff: Cleaner
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')

        for customer in customers:
            Customer.watch_movie(customer, movie_name)

        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)
