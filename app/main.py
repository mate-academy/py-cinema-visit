from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from typing import List, Dict


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customer_objects = [
        Customer(name=data["name"], food=data["food"]) for data in customers
    ]
    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    # Selling products
    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # Movie session
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_obj
    )
