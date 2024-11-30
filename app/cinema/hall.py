from typing import List


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self,
                      movie_name: str,
                      customers: List["Customer"],
                      cleaning_staff: "CleaningStaff") -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie(movie=movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(hall_number=self.number)


class Customer:
    def watch_movie(self, movie: str) -> None:
        print(f"Watching movie: {movie}")


class CleaningStaff:
    def clean_hall(self, hall_number: int) -> None:
        print(f"Cleaning hall number {hall_number}")
