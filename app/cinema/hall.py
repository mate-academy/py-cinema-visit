from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self,
                      movie_name: str,
                      customers: list[Customer | dict],
                      cleaning_staff: Cleaner) -> None:

        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            if isinstance(customer, Customer):
                customer.watch_movie(movie_name)
            else:
                create_customer = Customer(customer)
                create_customer.watch_movie(movie_name)

        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)
