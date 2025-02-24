from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:

    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str
                      , customers: list
                      , cleaning_staff: Cleaner) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            Customer.watch_movie(self=customer, movie=movie_name)
        print(f'"{movie_name}" ended.')
        Cleaner.clean_hall(self=cleaning_staff, hall_number=self.number)
