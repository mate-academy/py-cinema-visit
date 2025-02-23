from __future__ import annotations


class CinemaHall:

    def __init__(self, number: int):
        self.number = number

    def movie_session(self,
            customers: list,
            hall_number: int,
            cleaning_staff: Cleaner,
            movie_name: str):
        print(f"{movie_name} starts in hall {hall_number}!")
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f"{movie_name} ended in hall {hall_number}!")
        cleaning_staff.clean_hall(hall_number)

