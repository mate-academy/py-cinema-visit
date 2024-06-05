from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init_(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: list[Customer], cleaning_stuff: Cleaner):
        print(f"{movie_name} starts in the hall {self.number}")
        for customer in customers:
            customer.watch_movie(movie=movie_name)
        print(f"{movie_name} ends")
        cleaning_stuff.clean_hall(hall_number=self.number)

