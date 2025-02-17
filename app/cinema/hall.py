from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self,
                      movie_title: str,
                      customers: list[Customer],
                      cleaning_staff: Cleaner) -> None:
        print(f"\"{movie_title}\" started in hall number {self.number}.")
        for customer in customers:
            customer.watch_movie(movie_title)
        print(f"\"{movie_title}\" ended.")
        cleaning_staff.clean_hall(self.number)
