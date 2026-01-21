from app.people.cinema_staff import Cleaner


class CinemaHall:

    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self, movie_name: str, customer: list, cleaning_stuff: Cleaner
    ) -> None:
        print(f'\"{movie_name}\" started in hall number {self.number}.')
        for pearson in customer:
            pearson.watch_movie(movie_name)
        print(f'\"{movie_name}\" ended.')
        cleaner = cleaning_stuff
        cleaner.clean_hall(self.number)
