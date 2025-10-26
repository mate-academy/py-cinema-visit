from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, hall_number: int) -> None:
        self.hall_number = hall_number

    def movie_session(self, movie_name: str, customers: list[Customer], cleaning_staff: Cleaner) -> None:
        print(f"\"{movie_name}\" started in hall number {self.hall_number}.")
        customer = [Customer(customer.name, customer.food).watch_movie(movie_name) for customer in customers]
        print(f"\"{movie_name}\" ended.")
        cleaning_staff.clean_hall(self.hall_number)