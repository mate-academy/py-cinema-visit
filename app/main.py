from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner_name: str,
    movie: str
) -> None:
    customer_objects: List[Customer] = []

    for customer in customers:
        customer_obj = Customer(name=customer["name"], food=None)
        CinemaBar.sell_product(product=customer["food"], customer=customer_obj)
        customer_objects.append(customer_obj)

    staff: Cleaner = Cleaner(name=cleaner_name)

    hall: CinemaHall = CinemaHall(number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=staff
    )
