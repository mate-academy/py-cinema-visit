from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from typing import List, Dict, Any


def cinema_visit(
        customers: List[Dict[str, Any]],
        hall_number: int,
        cleaner_name: str,
        movie: str
) -> None:

    hall = CinemaHall(hall_number=hall_number)
    cleaner = Cleaner(name=cleaner_name)

    customer_instances = []
    for i in customers:
        customer = Customer(name=i["name"], food=i["food"])
        customer_instances.append(customer)
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner
    )
