from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, nm: str, css: list[Customer], cl: Cleaner) -> None:
        print(f"\"{nm}\" started in hall number {self.number}.")
        for customer in css:
            customer.watch_movie(nm)
        print(f"\"{nm}\" ended.")
        cl.clean_hall(self.number)
