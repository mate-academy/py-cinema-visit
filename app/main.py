from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: List[Dict[str, str]], hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_objects: List[Customer] = []
    for data in customers:
        customer = Customer(data["name"], data["food"])
        customer_objects.append(customer)
        CinemaBar.sell_product(customer.food, customer)

    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(movie, customer_objects, cleaning_staff)
