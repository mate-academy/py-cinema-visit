class CinemaHall:

    def __init__(self, number):
        self.number = number

    def movie_session(self, movie_name, customers, cleaner):
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaner.clean_hall(self.number)
