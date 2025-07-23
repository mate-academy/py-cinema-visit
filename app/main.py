from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from typing import List, Dict


def cinema_visit(customers: List[Dict[str, str]],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_instances: List[Customer] = []

    for data in customers:
        customer = Customer(name=data["name"], food=data["food"])
        customer_instances.append(customer)
        CinemaBar.sell_product(product=customer.food, customer=customer)

    cleaner_instance = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
