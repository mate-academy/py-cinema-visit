from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

from typing import List


def cinema_visit(customers: List[Customer], hall_number: int, cleaner: Cleaner, movie: str) -> None:
    ...

    """
    Function to manage serving a movie in a cinema hall.

    Args:
        customers (List[Customer]): List of customers attending.
        hall_number (int): The hall number where the movie is being shown.
        cleaner (Cleaner): Cleaner assigned to the hall.
        movie (str): The movie to be played.
    """
    hall = CinemaHall(hall_number, cleaner, movie)
    hall.clean_hall()

    for customer in customers:
        hall.admit_customer(customer)
        CinemaBar.serve_food(customer)

