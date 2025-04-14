from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:

    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: Customer,
            cleaning_staff: list[Cleaner]
    ) -> None:
        if not all(isinstance(customer, Customer) for customer in customers):
            raise ValueError
        if not isinstance(cleaning_staff, Cleaner):
            raise ValueError
        print(f"\"{movie_name}\" started in hall number {self.number}.")
        for customer in customers:
            customer.watch_movie(movie_name)

        print(f"\"{movie_name}\" ended.")

        cleaning_staff.clean_hall(self.number)
