from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number):
        self.number = number

    def movie_session(self, movie_name, customers, cleaning_staff):
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            print(f'{customer.name} is watching "{movie_name}".')
        print(f'"{movie_name}" ended.')
        Cleaner.clean_hall(self=cleaning_staff, hall_number=self.number)
