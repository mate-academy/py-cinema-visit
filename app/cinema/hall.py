from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self,
                      movie_title: str,
                      customers: list,
                      cleaner: Cleaner) -> str:
        print(f'"{movie_title}" started in hall number {self.number}.')
        for customer in customers:
            print(f'{customer.name} is watching "{movie_title}".')
        print(f'"{movie_title}" ended.')
        cleaner.clean_hall(self.number)
