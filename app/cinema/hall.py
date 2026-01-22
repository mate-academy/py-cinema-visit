from app.people import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self,
                      movie_name: str,
                      customers: list,
                      cleaning_staff: Cleaner) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')

        for customer in customers:
            print(f'{customer.name} is watching "{movie_name}".')

        print(f'"{movie_name}" ended.')
        cleaner_name = cleaning_staff.name
        hall_num = self.number
        print(f'Cleaner {cleaner_name} is cleaning hall number {hall_num}.')
