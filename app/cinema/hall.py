from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, mv: str, cus: list[Customer], cl: Cleaner) -> None:
        print(f'"{mv}" started in hall number {self.number}.')
        for pers in cus:
            pers.watch_movie(movie=mv)
        print(f'"{mv}" ended.')
        cl.clean_hall(hall_number=self.number)
