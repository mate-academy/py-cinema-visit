from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str) -> None:
        print(f"{movie_name} started in hall number {self.number}.")
        Customer.watch_movie()
        print(f"{movie_name} ended.")
        Cleaner.clean_hall(self.number)
