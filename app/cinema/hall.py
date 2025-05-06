from __future__ import annotations
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, hall_number: int) -> None:
        self.hall_number = hall_number

    def movie_session(self, movie_name: str, customers: list, cleaning_staff: Cleaner):
        print(f"\"{movie_name}\" started in hall number {self.hall_number}.")
        for person in customers:
            print(person.watch_movie(movie_name) + ".")
        return f"{movie_name} ended."


# hall = CinemaHall(hall_number=5)
# movie_name = "Madagascar"
# customers = [
#     Customer(name="Bob", food="Coca-cola"),
#     Customer(name="Alex", food="popcorn")
# ]
# cleaning_staff = Cleaner(name="Anna")
#
# hall.movie_session(movie_name=movie_name, customers=customers, cleaning_staff=cleaning_staff)
