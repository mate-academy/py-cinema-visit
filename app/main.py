from typing import List, Dict
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: List[Dict[str, str]],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_objects = []
    for customer in customers:
        customer_obj = Customer(name=customer["name"], food=customer["food"])
        customer_objects.append(customer_obj)
        CinemaBar.sell_product(product=customer["food"], customer=customer_obj)

    cleaner_obj = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_obj
    )
