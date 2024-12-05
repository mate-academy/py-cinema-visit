# app/main.py

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from typing import List, Dict


def cinema_visit(customers: List[Dict[str, str]],
                 hall_number: int, cleaner: str, movie: str) -> None:
    # Create instances of Customer and Cleaner
    customer_instances = [Customer
                          (name=customer["name"],
                           food=customer["food"]) for customer in customers]
    cleaner_instance = Cleaner(name=cleaner)

    # Sell food to customers
    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # Create an instance of CinemaHall and schedule the movie session
    hall = CinemaHall(hall_number)
    hall.movie_session(movie_name=movie,
                       customers=customer_instances,
                       cleaning_staff=cleaner_instance)
