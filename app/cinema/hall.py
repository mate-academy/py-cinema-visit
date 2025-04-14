class CinemaHall:
    def __init__(self, number: int) -> int:
        self.number = number

    def movie_session(
            self, movie_name: str, customers: list, cleaning_staff: str
    ) -> None:
        print(
            f'"{movie_name}" started in hall number {self.number}.')

        for customer in customers:
            customer.watch_movie(movie_name)

        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)


class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        print(f"Cleaning staff is cleaning the hall {hall_number}.")
