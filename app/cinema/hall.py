from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> str:
        self.number = number

    def movie_session(
            self,
            movie: str,
            customer_info: list[Customer],
            cleaning_staff: Cleaner,
    ) -> None:
        print(f'"{movie}" started in hall number {self.number}.')
        for customer in customer_info:
            customer.watch_movie(movie)

        print(f'"{movie}" ended.')
        cleaning_staff.clean_hall(self.number)
