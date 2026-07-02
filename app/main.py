from typing import Dict, List

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_instances = []
    for cust_data in customers:
        customer = Customer(name=cust_data["name"], food=cust_data["food"])
        customer_instances.append(customer)
        CinemaBar.sell_product(product=customer.food, customer=customer)

    cleaner_instance = Cleaner(name=cleaner)
    hall_instance = CinemaHall(number=hall_number)

    hall_instance.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
