class CinemaHall:
    def __init__(self, number):
        self.number = number

    def movie_session(self, movie_name, customers, cleaning_staff):
        # announce start
        print(f'"{movie_name}" started in hall number {self.number}.')
        # each customer watches movie
        for customer in customers:
            customer.watch_movie(movie_name)
        # announce end
        print(f'"{movie_name}" ended.')
        # cleaner cleans the hall
        cleaning_staff.clean_hall(hall_number=self.number)

