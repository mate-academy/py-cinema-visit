from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movies_name: str, customers: list[Customer], cleaning_staff: Cleaner):
        print(f"Movie {movies_name} is starting in hall {self.number}.")
        for customer in customers:
            customer.watch_movie(movies_name)
        print(f"Movie {movies_name} has ended in hall {self.number}.")
        cleaning_staff.clean_hall(self.number)





