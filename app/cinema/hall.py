class CinemaHall:
    def __init__(self, number: int) -> str:
        self.number = number

    def movie_session(self, movie_name: str,
                      customers: str,
                      cleaning_staff: str) -> str:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for client in customers:
            client.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)
