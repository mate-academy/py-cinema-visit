from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            move_name: str,
            customers: list[Customer],
            cleaning_staff: Cleaner
    ) -> None:
        print(f'"{move_name}" started in hall number {self.number}.')
        for person in customers:
            person.watch_movie(move_name)
        print(f'"{move_name}" ended.')
        cleaning_staff.clean_hall(self.number)
