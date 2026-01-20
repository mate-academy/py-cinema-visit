class CinemaHall:
    def __init__(self, number):
        self.number = number

    def movie_session(self,movie_name, customers, cleaning_staff):
        print(f"Movie '{movie_name}' is starting in hall {self.number}.")

        for customer in customers:
            customer.watch_movie(movie_name)

        print(f"Movie '{movie_name}' has ended in hall {self.number}.")

        cleaning_staff.clean_hall(self.number)