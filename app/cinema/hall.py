from app.people import customer
from app.people import cinema_staff


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str,
                      customers: list[customer.Customer],
                      cleaning_staff: cinema_staff.Cleaner) -> None:
        print(f'\"{movie_name}\" started in hall number {self.number}.')
        for person in customers:
            print(f'{person.name} is watching \"{movie_name}\".')
        print(f'\"{movie_name}\" ended.')
        cleaning_staff.clean_hall(self.number)
