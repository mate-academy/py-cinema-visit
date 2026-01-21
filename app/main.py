from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: List[Dict[str, str]],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = [Customer(**data) for data in customers]
    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    for customer in customer_instances:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customer_instances, cleaner_instance)
