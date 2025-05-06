from __future__ import annotations
from app.people.cinema_staff import Cleaner

class CinemaHall:
    def __init__(self, hall_number: int) -> None:
        self.hall_number = hall_number

    def movie_session(self, movie_name: str, customers: list, cleaning_staff: Cleaner):
        print(f"\"{movie_name}\" started in hall number {self.hall_number}.")
        for person in customers:
            print(person.watch_movie(movie_name) + ".")
        print(f"{movie_name} ended.")
        return f"Cleaner {cleaning_staff.name} is cleaning hall number {self.hall_number}."
