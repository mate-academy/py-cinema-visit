from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, film_name: str,
                      customers: list[Customer],
                      cleaning_staff: Cleaner) -> None:
        print(f'"{film_name}" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie(film_name)
        print(f'"{film_name}" ended.')
        cleaning_staff.clean_hall(self.number)
