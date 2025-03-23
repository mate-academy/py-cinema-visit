from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int):
        self.number = number

    def movie_session(self, movie_name: str,
                      customers: list,
                      cleaning_staff):
        print(f'"{movie_name}" started in hall number {self.number}.')

        # each one customer is watching film
        for customer in customers:
            customer.watch_movie(movie_name)

        print(f'"{movie_name}" ended.')

        # create Cleaner instance and clean the hall
        clean_staff = Cleaner(cleaning_staff.name)
        clean_staff.clean_hall(self.number)
