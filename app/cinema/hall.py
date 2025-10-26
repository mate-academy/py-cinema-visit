from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number
    def movie_session(self, movie_name: str, customers: list[Customer], cleaning_staff: Cleaner):
        print(f'"{movie_name}" started in hall.py number {self.number}.')
        for customer_values in customers:
            customer_values.watch_movie(movie=movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(hall_number=self.number)
