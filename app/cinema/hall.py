from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: list[Customer], cleaning_staff: Cleaner):
        print(F"\"{movie_name}\" started in hall number {self.number}.")
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f"\"{movie_name}\" ended.")
        cleaning_staff.clean_hall(self.number)





#This method prints about movie start,
# calls customers method watch_movie, prints about movie end, calls cleaner method clean_hall.
#So, we are expecting that everything listed above will be performed in movie_session function.