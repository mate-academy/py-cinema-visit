app/__init__.py
app/people/__init__.py

class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        print(f'{self.name} is watching "{movie}".')

class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")

from app.people.customer import Customer

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, hall_number: int) -> None:
        self.hall_number = hall_number

    def movie_session(
            self,
            movie_name: str,
            customers: list[Customer],
            cleaning_staff: Cleaner
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.hall_number}.')
        for customer in customers:
            customer.watch_movie(movie=movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(hall_number=self.hall_number)

class CinemaBar:
    @staticmethod
    def sell_product(customer: Customer, product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = [
        Customer(name=c["name"], food=c["food"])
        for c in customers
    ]

    for customer in customer_instances:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaning_staff
    )
