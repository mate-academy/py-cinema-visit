class CinemaHall:
    def __init__(self, hall_number: int) -> None:
        self.hall_number = hall_number

    def movie_session(self, movie_name: str, customers: list, cleaning_staff) -> None:
        print(f'"{movie_name}" started in hall number {self.hall_number}.')
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.hall_number)
