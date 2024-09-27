class CinemaHall:
    def __init__(self, number):
        self.number = number

    def movie_session(self, movie_name, customers, cleaning_staff):
        print(f'"{movie_name}" started in hall number {self.number}.')

        for customer in customers:
            customer.watch_movie(movie_name)

        print(f'"{movie_name}" ended.')

        cleaning_staff.clean_hall(self.number)
