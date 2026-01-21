from typing import List

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: List[Customer],
        hall_number: int,
        cleaner_name: str,
        movie: str
) -> None:
    cinema_bar = CinemaBar()
    cleaner = Cleaner(name=cleaner_name)

    customer_objects = []
    for customer_info in customers:
        customer = Customer(
            name=customer_info["name"],
            food=customer_info["food"]
        )
        customer_objects.append(customer)
        cinema_bar.sell_product(product=customer.food, customer=customer)

    cinema_hall = CinemaHall(number=hall_number)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner
    )
