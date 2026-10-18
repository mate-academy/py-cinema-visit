from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
        self,
        movie_name: str,
        customers: list[Customer],
        cleaning_staff: Cleaner
    ) -> None:
        quote = '"'
        print(
            f"{quote}{movie_name}{quote} started in hall number "
            f"{self.number}."
        )
        for customer in customers:
            customer.watch_movie(movie=movie_name)

        print(f"{quote}{movie_name}{quote} ended.")

        cleaning_staff.clean_hall(hall_number=self.number)
