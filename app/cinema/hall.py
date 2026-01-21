from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list[Customer],
            cleaning_staff: Cleaner
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            print(f'{customer.name} is watching "{movie_name}".')
        print(f'"{movie_name}" ended.')
        print(
            f"Cleaner {cleaning_staff.name} "
            f"is cleaning hall number {self.number}."
        )


if __name__ == "__main__":
    customers = [
        Customer("Bob", "Coca-cola"),
        Customer("Alex", "popcorn")
    ]
    hall_number = 5
    cleaner_name = "Anna"
    cleaner = Cleaner(cleaner_name)
    movie = "Madagascar"
    certain_visitor = CinemaHall(hall_number)
    certain_visitor.movie_session(movie, customers, cleaner)
