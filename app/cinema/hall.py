from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, hall_number: int = None, *, number: int = None) -> None:
        self.hall_number = hall_number if hall_number is not None else number
        self.number = self.hall_number  # Add this line to satisfy the test
        if self.hall_number is None:
            raise ValueError("Must provide either hall_number or number")

    def movie_session(
            self,
            movie_name: str,
            customers: list,
            cleaning_staff: Cleaner
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.hall_number}.')
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.hall_number)
