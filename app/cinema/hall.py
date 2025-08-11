class CinemaHall:
    def __init__(self, number):
        self.number = number

    def movie_session(self, movie, customers, cleaning_staff):
        print(f'"{movie}" started in hall number {self.number}.')

        for customer in customers:
            customer.watch_movie(movie)

        print(f'"{movie}" ended.')
        cleaning_staff.clean_hall(self.number)