from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: list[Customer],
                      cleaning_stuff: Cleaner) -> None:
        staff = Cleaner(cleaning_stuff.name)
        print(f'\"{movie_name}\" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'\"{movie_name}\" ended.')
        staff.clean_hall(self.number)
