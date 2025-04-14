from app.people.customers import Customer as cst
from app.people.cinema_staff import Cleaner as cl


class CinemaHall:
    def __init__(self, number):
        self.number = number
    
    
    def movie_session(self, movie_name: str, customers: list, cleaning_staff: list):
        if not all(isinstance(customer, Customer) for customer in customers):
            raise TypeError("All customers must be instances of Customer.")
        if not all(isinstance(staff, Cleaner) for staff in cleaning_staff):
            raise TypeError("All cleaning_staff must be instances of Cleaner.")

        print(f"Movie '{movie_name}' starts in hall {self.number}.")
        for customer in customers:
            customer.cst.watch_movie(movie_name)
        print(f"Movie '{movie_name}' ends!")
        for cleaner in cleaning_staff:
            cleaner.cl.clean_hall(self.number)
