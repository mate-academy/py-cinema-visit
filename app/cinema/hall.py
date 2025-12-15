from app.people.cinema_staff import Cleaner

class CinemaHall:
    def __init__(self, number: int):
        self.number = number


    def movie_session(self, movie_name:str, customers: list, cleaning_staff: Cleaner):
        print(f"Movie {movie_name} started.")
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f"Movie {movie_name} ended.")
        cleaning_staff.clean_hall(self.number)
