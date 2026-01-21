from typing import List
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number
        self.hall_number = number

    def movie_session(self, movie_name: str,
                      customers: List[Customer],
                      cleaning_staff: Cleaner) -> None:
        print(f'"{movie_name}" started in hall number {self.hall_number}.')
        for cust in customers:
            cust.watch_movie(movie=movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(hall_number=self.hall_number)


if __name__ == "__main__":
    hall = CinemaHall(number=5)
    movie_name = "Madagascar"
    customers = [
        Customer(name="Bob", food="Coca-cola"),
        Customer(name="Alex", food="popcorn")
    ]
    cleaning_staff = Cleaner(name="Anna")

    hall.movie_session(movie_name=movie_name,
                       customers=customers,
                       cleaning_staff=cleaning_staff)
