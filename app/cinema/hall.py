from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    """
    Class representing cinema hall
    """
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self,
                      movie_name: str,
                      customers: list[Customer],
                      cleaning_staff: Cleaner) -> None:
        """
        Function that runs movie session in cinema hall. Informs
        about starting movie, watching it by customers, ending movie
        and clening the hall
        :param movie_name: movie name to be played
        :param customers: list of customers
        :param cleaning_staff: staff member for cleaning hall
        :return: None
        """
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)
