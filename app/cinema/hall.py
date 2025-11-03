class CinemaHall:
    def __init__(self, hall_number) :
        self.hall_number = hall_number
    def movie_session(self, movie_name, customers, cleaning_staff):
        print(f'"{movie_name}" started in hall number {self.hall_number}.')

        for customer in customers:
            print(f'{customer.name} is watching "{movie_name}".')
        print(f'"{movie_name}" ended.')
        print(f'Cleaner {cleaning_staff.name} is cleaning hall number {self.hall_number}.')