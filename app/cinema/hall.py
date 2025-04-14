class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number: int = number

    def movie_session(self, movie_name: str, customers: list[None], cleaning_staff: None) -> None:  # noqa: E501
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie(movie=movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(hall_number=self.number)
