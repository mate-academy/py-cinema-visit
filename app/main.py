from typing import Dict, List

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customer_objs: List[Customer] = [
        Customer(name=item["name"], food=item["food"]) for item in customers
    ]

    for customer in customer_objs:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    CinemaHall(hall_number=hall_number).movie_session(
        movie_name=movie,
        customers=customer_objs,
        cleaning_staff=Cleaner(name=cleaner),
    )

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


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: "Customer") -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")


from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from app.people.customer import Customer
    from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, hall_number: int) -> None:
        self.hall_number = hall_number

    def movie_session(
        self,
        movie_name: str,
        customers: List["Customer"],
        cleaning_staff: "Cleaner",
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.hall_number}.')
        for customer in customers:
            customer.watch_movie(movie=movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(hall_number=self.hall_number)
