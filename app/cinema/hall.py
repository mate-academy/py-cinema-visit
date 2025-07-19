from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, hall_number: int) -> None:
        self.hall_number = hall_number
        # Видалено надлишковий self.number = hall_number, оскільки ви просили використовувати hall_number
        # Якщо інші частини вашого коду все ще покладаються на 'self.number', вам потрібно буде вирішити, який атрибут використовувати послідовно.

    def movie_session(
        self,
        movie_name: str,
        customers: list[Customer],
        cleaning_staff: Cleaner
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.hall_number}.')
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.hall_number)