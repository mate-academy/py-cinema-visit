from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: List[Dict[str, str]], hall_number: int,
                 cleaner: str, movie: str) -> None:
    if not isinstance(customers, list):
        raise TypeError("customers should be a list")

    customer_objects: List[Customer] = []

    # Продажа продуктов
    for customer in customers:
        customer_instance = Customer(name=customer["name"],
                                     food=customer["food"])
        CinemaBar.sell_product(product=customer_instance.food,
                               customer=customer_instance)

        customer_objects.append(customer_instance)

    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(cleaner)

    hall.movie_session(movie_name=movie, customers=customer_objects,
                       cleaning_staff=cleaning_staff)
