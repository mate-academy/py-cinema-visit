from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from typing import Any


def cinema_visit(
        customers: list, number: int, cleaner: str, movie: str
    ) -> Any:
    customer_instances = [
        Customer(
            name=customer["name"], food=customer["food"]
        ) for customer in customers
    ]

    cleaner_instance = Cleaner(name=cleaner)

    hall_instance = CinemaHall(number=number)

    for customer in customer_instances:
        CinemaBar.sell_product(
        product=customer.food, customer=customer
    )

    hall_instance.movie_session(
        movie_name=movie, customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
