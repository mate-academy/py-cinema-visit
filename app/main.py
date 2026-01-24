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
    customer_objects = [
        Customer(name=data["name"], food=data["food"])
        for data in customers
    ]
    cleaner_obj = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)
    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_obj,
    )
