from app.people import customer
from app.people import cinema_staff


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
        self,
        movie_name: str,
        customers: list[customer.Customer],
        cleaning_staff: str
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for custom in customers:
            customer.Customer.watch_movie(custom, movie_name)
        print(f'"{movie_name}" ended.')
        cinema_staff.Cleaner.clean_hall(cleaning_staff, self.number)
        pass
