from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:

    def __init__(self, number: int) -> None:
        self.number = number
    # This class should have only one method `movie_session`, that
    # takes `movie_name`, `customers` - list of a customers
    # (`Customer` instances), `cleaning_staff` - cleaner (`Cleaner`
    # instance).

    def movie_session(self, movie_name: str,
                      customers: list[Customer], cleaner: Cleaner) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaner.clean_hall(self.number)

    # This method prints about movie start, calls
    # customers method `watch_movie`,
    # prints about movie end,
    # calls cleaner method `clean_hall`.
    # So, we are expecting
    # that everything listed above
    # will be performed in `movie_session` function.
