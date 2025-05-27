from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: "Customer",
            cleaning_staff: "Cleaner"
    ) -> None:
        Customer.watch_movie(movie_name)
        Cleaner.clean_hall(self.number)
