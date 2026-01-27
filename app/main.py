from typing import List, Dict

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_objects: List[Customer] = []
    for data in customers:
        customer = Customer(name=data["name"], food=data["food"])
        customer_objects.append(customer)

    hall = CinemaHall(number=hall_number)
    cleaner_obj = Cleaner(name=cleaner)

    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_obj
    )
