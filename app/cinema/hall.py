class CinemaHall:
    def __init__(self, hall_number: int) -> int:
        self.number = hall_number

    def movie_session(self, movie_name: str,
                      customers: str, cleaning_staff: str) -> any:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie(movie=movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(hall_number=self.number)
