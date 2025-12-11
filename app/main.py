from typing import List, Dict
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: List[Dict[str, str]],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    cleaner_instance = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)
    customer_instances: List[Customer] = []

    for customer_data in customers:
        customer_obj = Customer(name=customer_data["name"],
                                food=customer_data["food"])
        customer_instances.append(customer_obj)
        CinemaBar.sell_product(
            product=customer_obj.food, customer=customer_obj)

    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
