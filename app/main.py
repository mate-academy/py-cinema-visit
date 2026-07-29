"""
main.py

Entry point that simulates a customer's visit to the cinema.
"""

from typing import Dict, List

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    """
    Simulate a full cinema visit: sell food to customers, run the movie
    session, and have the cleaner clean the hall afterwards.

    :param customers: list of dict, each dict has 'name' and 'food' keys
        describing a customer.
    :param hall_number: int, the number of the hall in the cinema.
    :param cleaner: str, the name of the cleaner who will clean the hall
        after the movie session.
    :param movie: str, the name of the movie to be shown.
    """
    customer_instances = [
        Customer(name=customer_data["name"], food=customer_data["food"])
        for customer_data in customers
    ]

    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    cinema_hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaning_staff,
    )
