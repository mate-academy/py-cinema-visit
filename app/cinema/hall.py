from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: list, cleaning_staff: "Cleaner") -> None:
        print(f"Movie {movie_name} is starting at hall {self.number}")
        for customer in customers:
            customer.watch.movie()

        print(f"Movie {movie_name} has ended at hall {self.number}")
        cleaning_staff.clean_hall()
