from app.people.cinema_staff import Cleaner
from app.people.customer import Customer

class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number
    def movie_session(self, movie_name: str, customers: list, cleaning_staff: Cleaner) -> None:

