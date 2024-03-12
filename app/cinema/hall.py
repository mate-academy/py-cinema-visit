from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

class CinemaHall:
    def __init__(self, number: int):
        self.number = number

    def movie_session(self, movie_name: str, customers: list[Customer], cleaning_staff: Cleaner):
        print(f"Movie session for {movie_name} started in Hall {self.number}.")

        for customer in customers:
            customer.watch_movie(movie_name)

        print(f"Movie session for {movie_name} ended in Hall {self.number}.")
        cleaning_staff.clean_hall()
