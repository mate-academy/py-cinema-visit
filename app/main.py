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
    customer_objects = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]
    cinema_bar = CinemaBar()

    for customer in customer_objects:
        cinema_bar.sell_product(
            product=customer.food,
            customer=customer
        )

    hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_instance
    )
