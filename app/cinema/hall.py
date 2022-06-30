from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:

    def __init__(self, number):
        self.number = number

    def movie_session(self, movie_name, customers: list, cleaner):
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            Customer.watch_movie(customer, movie_name)
        print(f'"{movie_name}" ended.')
        Cleaner.clean_hall(cleaner, self.number)
