class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie: str, customers: list, cleaner) -> None:
        cleaner.clean_hall(self.number)
        for customer in customers:
            customer.watch_movie(movie)
