from __future__ import annotations

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list[Customer],
            cleaning_staff: Cleaner,
    ) -> None:

        print(f'\"{movie_name}\" started in hall number {self.number}.')

        for client in customers:
            client.watch_movie(movie_name)

        print(f'\"{movie_name}\" ended.')

        cleaning_staff.clean_hall(self.number)


if __name__ == "__main__":
    cin_hall = CinemaHall(number=55)
    customers = [Customer("Bob", "Coca-cola"), Customer("Alex", "popcorn")]
    stf = Cleaner("Anna")
    movie = "Madagaskar"
    cin_hall.movie_session(movie, customers, stf)
