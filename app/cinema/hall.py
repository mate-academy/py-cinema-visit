from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self,
                      movie_name: str,
                      customers: list[Customer],
                      cleaning_staff: Cleaner) -> None:

        print(f'\"{movie_name}\" started in hall number {self.number}.')

        lst_instances = []

        for visitor in customers:
            visitor_instance = Customer(visitor.name)
            lst_instances.append(visitor_instance)

        for inst in lst_instances:
            inst.watch_movie(movie_name)

        print(f'\"{movie_name}\" ended.')

        staff = Cleaner(cleaning_staff.name)
        staff.clean_hall(self.number)
