# app/cinema/hall.py

class CinemaHall(object):
    def __init__(self, hall_number):
        self.hall_number = hall_number

    def movie_session(self, movie_name, customers, cleaning_staff):
        print('"{}" started in hall number {}.'.format(
            movie_name, self.hall_number))

        for customer in customers:
            customer.watch_movie(movie_name)

        print('"{}" ended.'.format(movie_name))
        cleaning_staff.clean_hall(self.hall_number)
