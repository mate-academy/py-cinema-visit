from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: List[Dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_instances = []
    for customer_dict in customers:
        customer = Customer(
            name=customer_dict.get("name"),
            food=customer_dict.get("food")
        )
        customers_instances.append(customer)

    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)

    for customer in customers_instances:
        cinema_bar.sell_product(customer, customer.food)

    hall.movie_session(movie, customers_instances, cleaner)
