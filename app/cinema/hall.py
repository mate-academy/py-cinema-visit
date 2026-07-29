class CinemaHall:
    def __init__(self, hall_number: int):
        self.hall_number = hall_number
    def movie_session(self, movie_name: str, customers: list, cleaning_staff):
        print(f'"{movie_name}" started in hall number {self.hall_number}.')
        for customer in customers:
            customer.watch_movie(movie=movie_name) # You'll need to import Customer here later
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(hall_number=self.hall_number) # You'll need to import Cleaner here later
