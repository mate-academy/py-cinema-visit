class CinemaHall:

    def __init__(self, number):
        self.number = number

    def movie_session(self, movie, new, cleaning_staff):
        print(f'"{movie}" started in hall number {self.number}.')
        for cust in new:
            cust.watch_movie(movie)
        print(f'"{movie}" ended.')
        cleaning_staff.clean_hall(self.number)
