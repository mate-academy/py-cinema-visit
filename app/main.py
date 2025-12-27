from typing import List, Dict

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: List[Dict[str, str]],
                 hall_number: int,
                 cleaner: str, movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    customer_instances = []
    for customer_data in customers:
        customer_instance = Customer(name=customer_data["name"],
                                     food=customer_data["food"])
        cinema_bar.sell_product(product=customer_instance.food,
                                customer=customer_instance)
        customer_instances.append(customer_instance)

    cinema_hall.movie_session(movie_name=movie, customers=customer_instances,
                              cleaning_staff=cleaning_staff)
