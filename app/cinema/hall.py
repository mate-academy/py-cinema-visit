from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(
        self,
        hall_number: int | None = None,
        *,
        number: int | None = None
    ) -> None:
        self.number = (
            hall_number if hall_number is not None else number
        )

    def movie_session(
        self,
        movie_name: str,
        customers: list[Customer],
        cleaning_staff: Cleaner
    ) -> None:
        print(
            f'"{movie_name}" started in '
            f"hall number {self.number}."
        )

        for customer in customers:
            customer.watch_movie(movie_name)

        print(f'"{movie_name}" ended.')

        cleaning_staff.clean_hall(self.number)
