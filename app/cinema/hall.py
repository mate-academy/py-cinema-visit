from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self,
                      movie_name: str,
                      customers: list,
                      cleaning_staff: Cleaner) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)

# hall = CinemaHall(number=5)
# movie_name = "Madagascar"
# customers = [
#     Customer(name="Bob", food="Coca-cola"),
#     Customer(name="Alex", food="popcorn")
# ]
# cleaning_staff = Cleaner(name="Anna")
#
# hall.movie_session(movie_name=movie_name,
# customers=customers, cleaning_staff=cleaning_staff)
