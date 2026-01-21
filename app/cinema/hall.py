from app.people import customer as p_customer
from app.people import cinema_staff as p_cinema_staff


class CinemaHall:
    def __init__(self, number : int) -> None:
        self.number = number

    def movie_session(self, movie_name : str,
                      customers : list[p_customer.Customer],
                      cleaner : p_cinema_staff.Cleaner) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            current_cust = p_customer.Customer(customer.name, customer.food)
            current_cust.watch_movie(movie_name)
        print(f'"{movie_name}\" ended.')
        cleaner.clean_hall(self.number)
