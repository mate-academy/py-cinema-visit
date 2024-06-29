from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str,
                      customers: list,
                      cleaning_staff: Cleaner) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for cinema_customer in customers:
            if isinstance(cinema_customer, dict):
                cinema_customer_obj = Customer(cinema_customer["name"],
                                               cinema_customer["food"])
                cinema_customer_obj.watch_movie(movie_name)
            if isinstance(cinema_customer, Customer):
                cinema_customer.watch_movie(movie_name)

        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)
