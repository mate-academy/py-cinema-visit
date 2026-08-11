from typing import Any


class CinemaHall:
    def __init__(self, number: int = None, hall_number: int = None) -> None:
        hall_num = number if number is not None else hall_number
        self.hall_number = hall_num
        self.number = hall_num

    def movie_session(
        self, movie_name: str, customers: list[Any], cleaning_staff: Any
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.hall_number}.')
        for customer in customers:
            customer.watch_movie(movie=movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(hall_number=self.hall_number)
