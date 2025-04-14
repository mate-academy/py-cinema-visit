from typing import Dict, List

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: List[Dict[str, str]], hall_number: int,
                 cleaning_staff: str, movie_name: str) -> None:

    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaning_staff)
    customer_instances = [Customer(**customer) for customer in customers]

    # I decided to make "customer_instances" more compact, instead of:
    # customer_instances = [
    #    Customer(name=customer['name'],
    #             food=customer['food'])
    #    for customer in customers
    # ],
    # I sacrificed readability for compactness.

    for customer in customer_instances:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    cinema_hall.movie_session(
        movie_name=movie_name,
        customers=customer_instances,
        cleaning_staff=cleaner,
    )


if __name__ == "__main__":
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    hall_number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"
    cinema_visit(customers=customers, hall_number=5,
                 cleaning_staff="Anna", movie_name="Madagascar")
