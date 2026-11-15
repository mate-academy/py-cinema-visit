from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, hall_number: int) -> None:
        self.hall_number = hall_number

    def movie_session(self, movie: str, customers: list,
                      cleaning_staff: Cleaner) -> None:
        print(f'"{movie}" started in hall number {self.hall_number}.')
        for customer in customers:
            customer.watch_movie(movie)
        print(f'"{movie}" ended.')
        cleaning_staff.clean_hall(self.hall_number)
