from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from typing import List, Dict


def cinema_visit(
        customers: List[Dict[str, str]],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_objects = []
    for customer_data in customers:
        customer_objects.append(
            Customer(customer_data["name"], customer_data["food"])
        )

    for customer_obj in customer_objects:
        CinemaBar.sell_product(customer_obj, customer_obj.food)

    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    hall.movie_session(movie, customer_objects, cleaner_obj)
