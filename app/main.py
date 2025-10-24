from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_objs = [Customer(name=c["name"], food=c["food"]) for c in customers]

    for c in customer_objs:
        CinemaBar.sell_product(product=c.food, customer=c)

    hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    hall.movie_session(movie_name=movie, customers=customer_objs, cleaning_staff=cleaning_staff)

class CinemaBar:
    @staticmethod
    def sell_product(product, customer):
        print(f"Cinema bar sold {product} to {customer.name}.")


class CinemaHall:
    def __init__(self, hall_number):
        self.hall_number = hall_number

    def movie_session(self, movie_name, customers, cleaning_staff):
        print(f'"{movie_name}" started in hall number {self.hall_number}.')
        for customer in customers:
            customer.watch_movie(movie=movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(hall_number=self.hall_number)


class Customer:
    def __init__(self, name, food):
        self.name = name
        self.food = food

    def watch_movie(self, movie):
        print(f'{self.name} is watching "{movie}".')


class Cleaner:
    def __init__(self, name):
        self.name = name

    def clean_hall(self, hall_number):
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
