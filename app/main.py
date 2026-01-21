from typing import Dict
from typing import List
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: List[Dict[str, str]], hall_number: int,
        cleaner: str, movie: str
) -> None:
    customer_objects = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    cleaner_objects = Cleaner(name=cleaner)
    hall_objects = CinemaHall(number=hall_number)

    for cust in customer_objects:
        CinemaBar.sell_product(product=cust.food, customer=cust)

    hall_objects.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_objects,
    )
