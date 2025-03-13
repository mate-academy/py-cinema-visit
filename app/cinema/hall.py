from app.people.customer import Customer
from app.people.cleaning_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
        self,
        movie_name: str,
        customers: list[Customer],
        cleaning_staff: Cleaner,
    ) -> None:
        print(f"Movie '{movie_name}' is starting in hall {self.number}.")

        for customer in customers:
            customer.watch_movie(movie_name)

        print(f"Movie '{movie_name}' has ended in hall {self.number}.")

        cleaning_staff.clean_hall(self.number)
