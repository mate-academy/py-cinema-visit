from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

class CinemaHall:
    def __init__(self, number) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: Customer, cleaning_staff: Cleaner):
        print(f"\"{movie_name}\" started in hall number {self.number}.")

        for customer in customers:
            customer.watch_movie(movie_name)

        print(f"\"{movie_name}\" ended.")
        cleaning_staff.clean_hall(self.number)


# from app.people.customer import Customer
# from app.people.cinema_staff import Cleaner
#
#
# class CinemaHall:
#     def __init__(self, hall_number: int) -> None:
#         self.hall_number = hall_number
#
#     @staticmethod
#     def movie_session(movie_name: str, customers: Customer, cleaning_staff: Cleaner) -> None:
#         print("Movie has started")
#         for customer in customers:
#             print(f"{customer.name} watching {movie_name}")
#         print("Movie has ended")
#         Cleaner.clean_hall(cleaning_staff)