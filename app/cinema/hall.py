from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    halls = []

    def __init__(self, number: int) -> None:
        self.number = number
        if self.number not in CinemaHall.halls:
            CinemaHall.halls.append(self.number)

    def movie_session(
            self,
            move_name: str,
            customers: list[Customer],
            cleaning_staff: Cleaner
    ) -> None:

        print(f'"{move_name}" started in hall number {self.number}.')

        for customer in customers:
            customer.watch_movie(move_name)

        print(f'"{move_name}" ended.')

        cleaning_staff.clean_hall(self.number)
