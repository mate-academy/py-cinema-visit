class CinemaHall:
    def __init__(self, hall_number: int):
        self.hall_number = hall_number

    def movie_session(self, movie: str, customers: list, cleaner):
        print(f'"{movie}" started in hall number {self.hall_number}.')

        for customer in customers:
            customer.watch_movie(movie)

        print(f'"{movie}" ended.')

        cleaner.clean_hall(self.hall_number)

