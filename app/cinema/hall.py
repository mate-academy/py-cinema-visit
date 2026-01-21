from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number) -> object:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list,
            cleaner: Cleaner
    ):
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            Customer.watch_movie(customer, movie_name)
        print(f'"{movie_name}" ended.')
        cleaner.clean_hall(self.number)
