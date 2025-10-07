from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def start_end_movie(self, movie_name: str, start_or_end: str) -> None:
        if start_or_end == "start":
            print(f"\"{movie_name}\" started in hall number {self.number}.")
        elif start_or_end == "end":
            print(f"\"{movie_name}\" ended.")

    def movie_session(
            self,
            movie_name: str,
            customers: list,
            cleaning_staff: Cleaner
    ) -> None:
        CinemaHall.start_end_movie(self, movie_name, "start")
        for customer in customers:
            Customer.watch_movie(customer, movie_name)
        CinemaHall.start_end_movie(self, movie_name, "end")
        Cleaner.clean_hall(cleaning_staff, self.number)
