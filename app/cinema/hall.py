from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number):
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list,
            cleaning_staff: Cleaner
    ):
        print(f'"{movie_name}" started in hall number {self.number}.')

        for customer in customers:
            customer.watch_movie(movie_name)

        print(f'"{movie_name}" ended.')

        Cleaner.clean_hall(cleaning_staff, self.number)
