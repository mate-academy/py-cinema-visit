from typing import List, Dict

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
        Customer(name=c["name"], food=c["food"])
        for c in customers
    ]

    for cust in customer_objects:
        CinemaBar.sell_product(
            product=cust.food,
            customer=cust,
        )

    cleaner_obj = Cleaner(name=cleaner)
    hall = CinemaHall(hall_number=hall_number)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_obj,
    )
