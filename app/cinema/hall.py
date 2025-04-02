from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self, movie_name: str, customers: list, cleaner: Cleaner
    ) -> None:
        # Prints about movie start
        print(f'\"{movie_name}\" started in hall number {self.number}.')
        # Iteration in list
        for customer in customers:
            # calls customers method watch_movie
            customer.watch_movie(movie_name)
        # Prints about movie end
        print(f'\"{movie_name}\" ended.')
        # Calls cleaner method clean_hall
        cleaner.clean_hall(self.number)
