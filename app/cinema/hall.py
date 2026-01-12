from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
        self, movie_name: str,
        customers: list[Customer],
        cleaning_staff: Cleaner
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)
        cinema_hall = CinemaHall(hall_number)
        cleaner = Cleaner(cleaner)
        for customer in customers:
            CinemaBar.sell_product(customer.food, customer)
        cinema_hall.movie_session(movie, customers, cleaner)