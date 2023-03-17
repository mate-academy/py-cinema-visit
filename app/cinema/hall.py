from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> str:
        self.number = number

    def movie_session(self,
                      movie_name: str,
                      customers: list[Customer],
                      cleaning_staff: Cleaner
                      ) -> str:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for i in customers:
            i.watch_movie(movie=movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)


if __name__ == "__main__":
    Bob = Customer(name="Bob", food="Coca-cola")
    Alex = Customer(name="Alex", food="popcorn")
    customers = [Bob, Alex]
    cinema_hall = CinemaHall(5)
    cleaner = Cleaner(name="Anna")
    cinema_hall.movie_session(movie_name="Madagascar",
                              customers=customers,
                              cleaning_staff=cleaner
                              )
