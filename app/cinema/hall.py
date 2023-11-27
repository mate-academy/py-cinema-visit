from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self,
                      movie_name: str,
                      customers: list,
                      cleaning_staff: Cleaner) -> None:
        print('"{}" started in hall number {}.'.format(movie_name,
                                                       self.number))
        for customer in customers:
            customer.watch_movie(movie_name)
        print('"{}" ended.'.format(movie_name))
        cleaning_staff.clean_hall(self.number)
