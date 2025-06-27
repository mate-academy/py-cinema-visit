from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from typing import List, Dict


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_instances: List[Customer] = [
        Customer(name=customer_dict["name"], food=customer_dict["food"])
        for customer_dict in customers
    ]

    for customer_instance in customer_instances:
        CinemaBar.sell_product(
            product=customer_instance.food,
            customer=customer_instance
        )

    hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
