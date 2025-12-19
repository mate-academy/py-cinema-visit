from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:

    def __init__(self, hall_number):
        self.hall_number = hall_number



    def movie_session(self, movie_name, customers, cleaning_staff):
        print(f"{movie_name} started in hall number {self.hall_number}")

        for customer in customers:
            customer.watch_movie(movie_name)

        print(f"{movie_name} ended")

        cleaning_staff.clean_hall(self.hall_number)
