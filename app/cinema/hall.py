from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:

    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list | Customer,
            cleaning_staff: int | Cleaner
    ) -> None:
        print(
            f"\"{movie_name}\" started in hall number {self.number}."
        )
        for customer in customers:
            if isinstance(customer, dict):
                customer_name = customer.get("name")
                print(f'{customer_name} is watching "{movie_name}".')
            else:
                customer.watch_movie(movie_name)
        print(f"\"{movie_name}\" ended.")
        if isinstance(cleaning_staff, str):
            print(
                f"Cleaner {cleaning_staff} "
                f"is cleaning hall number {self.number}."
            )
        else:
            cleaning_staff.clean_hall(self.number)
