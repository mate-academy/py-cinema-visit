from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:

    def __init__(self, number):
        self.number = number

    def movie_session(self, movie_name: str,
                      customers: list,
                      cleaning_staff: Cleaner):
        print(f"\"{movie_name}\" started in hall number {self.number}.")
        for costumer in customers:
            viewer = Customer(costumer.name, costumer.food)
            viewer.watch_movie(movie_name)
        print(f"\"{movie_name}\" ended.")
        cleaning_staff.clean_hall(self.number)
