from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self,
                      movie_name: str,
                      customers: list,
                      cleaning_staff: "Cleaner") -> None:
        print(f"\"{movie_name}\" started in hall number {self.number}.")
        # calls customers method `watch_movie`
        for customer in customers:
            customer.watch_movie(movie=movie_name)
        # prints about movie end
        print(f"\"{movie_name}\" ended.")
        # calls cleaner method `clean_hall`
        cleaning_staff.clean_hall(self.number)
