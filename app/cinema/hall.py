from typing import Optional


class CinemaHall:
    def __init__(self, hall_number: Optional[int] = None, number: Optional[int] = None) -> None:
        if number is None:
            number = hall_number
        self.number = number
        self.hall_number = number

    def movie_session(self, movie_name: str, customers: list, cleaning_staff) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie(movie=movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(hall_number=self.number)

