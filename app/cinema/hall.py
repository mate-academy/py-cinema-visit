class CinemaHall:
    def __init__(self, number: int) -> callable:
        self.number = number

    def movie_session(self, movie_name: str, customers: list,
                      cleaning_staff: str) -> callable:
        print(f'\"{movie_name}\" started in hall number {self.number}.')
        [customer.watch_movie(movie_name) for customer in customers]
        print(f'\"{movie_name}\" ended.')
        cleaning_staff.clean_hall(self.number)
