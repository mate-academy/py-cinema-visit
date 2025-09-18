class CinemaHall:
    def __init__(self, hall_number):
        # use hall_number everywhere
        self.hall_number = hall_number

    def movie_session(self, movie_name, customers, cleaning_staff):
        # keyword args and self.hall_number per spec
        print(f'"{movie_name}" started in hall number {self.hall_number}.')
        for customer in customers:
            customer.watch_movie(movie=movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(hall_number=self.hall_number)
