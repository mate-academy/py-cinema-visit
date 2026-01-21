from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self, movie_name: str,
            customers: list,
            cleaning_staff: Cleaner
    ) -> str:
        print(f'\"{movie_name}\" started in hall number {self.number}.')
        if isinstance(customers[0], dict):
            for customer in customers:
                custom = Customer(customer["name"], customer["food"])
                custom.watch_movie(movie_name)
        if isinstance(customers[0], Customer):
            for customer in customers:
                customer.watch_movie(movie_name)
        print(f'\"{movie_name}\" ended.')
        cleaning_staff.clean_hall(self.number)
