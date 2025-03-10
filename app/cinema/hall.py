from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie: str,
            customers: list,
            cleaning_stuff: Cleaner
    ) -> None:
        print(f'"{movie}" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie(movie)
        print(f'"{movie}" ended.')
        cleaning_stuff.clean_hall(self.number)
