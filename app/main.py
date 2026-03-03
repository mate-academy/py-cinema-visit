from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customer_objects = []
    for customer in customers:
        customer_obj = Customer(name=customer["name"], food=customer["food"])
        customer_objects.append(customer_obj)

    cleaner_obj = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)

    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_obj,
    )
