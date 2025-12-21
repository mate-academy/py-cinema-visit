from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: List[Dict[str, str]],
                 hall_number: int, cleaner: str, movie: str) -> None:
    customer_instances = []
    for example in customers:
        customer = Customer(example["name"], example["food"])
        customer_instances.append(customer)
        CinemaBar.sell_product(customer.food, customer)

    staff = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    hall.movie_session(movie, customer_instances, staff)
