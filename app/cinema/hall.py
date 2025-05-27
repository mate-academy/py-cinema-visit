# from app.people.customer import Customer
# from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list,
            cleaning_staff: "Cleaner"
    ) -> None:
        for _ in customers:
            _.watch_movie()
        Cleaner.clean_hall(self.number)
