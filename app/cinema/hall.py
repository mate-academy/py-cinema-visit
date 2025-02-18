from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from  typing import  List


class CinemaHall:

    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers:List[Customer], cleaning_staff:Cleaner) -> None:

        print(f'"{movie_name}" stated in hall {movie_name}')
        for customer in customers:
            customer.watch_movie(f'"{movie_name}"')
        print(f'"{movie_name}" ended')
        cleaning_staff.clean_hall(self.number)








