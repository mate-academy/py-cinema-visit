from app.people.cinema_staff import Cleaner
from app.people.customer import Customer

class CinemaHall:
    def __init__(self, hall_number: int) -> None:
        self.hall_number = hall_number
    def movie_session(self, movie_name: str, customers: list, cleaning_staff: Cleaner) -> None:
        print(f"Movie {movie_name} is starting in hall number {self.hall_number}")
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f"\"{movie_name}\" ended.")
        cleaning_staff.clean_hall(self.hall_number)


if __name__ == "__main__":
    hall = CinemaHall(hall_number=5)
    movie_name = "Madagascar"
    customers = [
        Customer(name="Bob", food="Coca-cola"),
        Customer(name="Alex", food="popcorn")
    ]
    cleaning_staff = Cleaner(name="Anna")

    hall.movie_session(movie_name=movie_name, customers=customers, cleaning_staff=cleaning_staff)