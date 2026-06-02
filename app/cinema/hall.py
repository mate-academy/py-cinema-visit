from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:

    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list[Customer],
            cleaning_staff: Cleaner
    ) -> None:
        message_start = f'"{movie_name}" started in hall number {self.number}.'
        print(message_start)

        for customer in customers:
            customer.watch_movie(movie_name)

        message_end = f'"{movie_name}" ended.'
        print(message_end)
        cleaning_staff.clean_hall(self.number)
