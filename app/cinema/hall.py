class CinemaHall:
    def __init__(self, number: int) -> None:
        self.hall_number = number
        self.number = number


    def movie_session(
            self,
            movie_name: str,
            customers: list,
            cleaning_staff: None
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.hall_number}.')
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.hall_number)
