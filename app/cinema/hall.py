class CinemaHall:
    def __init__(self, hall_number):
        self.hall_number = hall_number

    def movie_session(self, movie_name: str, customers: list, cleaning_staff):
        print(f"\"{movie_name}\" started in hall number {self.hall_number}.")
        for i in customers:
            i.watch_movie(movie_name)
        print(f"\"{movie_name}\" ended.")
        cleaning_staff.clean_hall(self.hall_number)
