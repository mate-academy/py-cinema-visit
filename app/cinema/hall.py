from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
        self,
        movie_name: str,
        customers: list[Customer],
        cleaning_staff: Cleaner,
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')

        for customer in customers:
            customer.watch_movie(movie_name)

        print(f'"{movie_name}" ended.')

        cleaning_staff.clean_hall(hall_number=self.number)


# if __name__ == '__main__':
#     customer1 = Customer(name="Bob", food="Coca-cola")
#     customer2 = Customer(name="Alex", food="popcorn")
#     customer3 = Customer(name="John", food="chips")
#
#     cleaner = Cleaner(name="Anna")
#
#     hall = CinemaHall(hall_number=5)
#
#     hall.movie_session(
#         movie_name="Madagascar",
#         customers=[customer1, customer2, customer3],
#         cleaning_staff=cleaner
#     )
