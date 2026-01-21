from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

import sys
import os

# Füge das Projekt-Root-Verzeichnis zum Python-Pfad hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"


def cinema_visit(customers: list[dict], hall_number: int,
                 cleaner: str, movie: str) -> None:
    # write you code here
    cus_list = []
    for customer in customers:
        cus = Customer(customer["name"], customer["food"])
        cus_list.append(cus)
        CinemaBar.sell_product(cus.food, cus)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, cus_list, Cleaner(cleaner))
