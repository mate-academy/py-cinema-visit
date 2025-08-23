from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from typing import List


class CinemaHall:
    def __init__(self, hall_number: int) -> None:
        self.hall_number = hall_number

    def movie_session(
        self,
        movie_name: str,
        customers: List[Customer],
        cleaning_staff: List[Cleaner]
    ) -> None:

        print(f'\"{movie_name}\" started in hall number {self.hall_number}.')

        if not isinstance(cleaning_staff, list):
            cleaning_staff = [cleaning_staff]

        for customer in customers:
            print(f'{customer.name} is watching \"{movie_name}\".')

        print(f'\"{movie_name}\" ended.')

        for worker in cleaning_staff:
            worker.clean_hall(self.hall_number)
