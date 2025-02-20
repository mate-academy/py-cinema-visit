from typing import List, Dict

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: List[Dict[str, str]],
                 hall_number: int, cleaner: str, movie: str) -> None:

    customer_objects = [Customer(name=c["name"],
                                 food=c["food"]) for c in customers]
    hall = CinemaHall(hall_number)
    cleaner_object = Cleaner(name=cleaner)

    for customer in customer_objects:
        CinemaBar.sell_product(customer.food, customer)

    hall.movie_session(movie, customer_objects, cleaner_object)
