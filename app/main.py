from typing import List, Dict
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: List[Dict[str, str]],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cleaning_staff_instance = Cleaner(name=cleaner)

    customer_instances = []
    for data in customers:
        customer = Customer(name=data["name"], food=data["food"])
        customer_instances.append(customer)

    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall_instance = CinemaHall(hall_number=hall_number)

    hall_instance.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaning_staff_instance,
    )
