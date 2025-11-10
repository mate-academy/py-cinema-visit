from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, hall_number: int) -> None:
        self.hall_number = hall_number

    def movie_session(self, movie_name: str, customers: list[Customer], cleaning_staff: Cleaner) -> None:
        print(f"In cinema hall {self.hall_number} started movie \"{movie_name}\".")
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f"Movie \"{movie_name}\" in cinema hall {self.hall_number} is ended.")
        cleaning_staff.clean_hall(self.hall_number)
