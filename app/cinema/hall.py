from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall():
    def __init__(self, *args, **kwargs) -> None:
        if args:
            self.number = args[0]
        elif "number" in kwargs:
            self.number = kwargs["number"]
        elif "hall_number" in kwargs:
            self.number = kwargs["hall_number"]

    def movie_session(self,
                      movie_name: str,
                      customers: list["Customer"],
                      cleaning_staff: "Cleaner") -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')

        for customer in customers:
            customer.watch_movie(movie_name)

        print(f'"{movie_name}" ended.')

        cleaning_staff.clean_hall(self.number)
