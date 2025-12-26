from typing import List

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: List[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customer_instances = [Customer(
        name=customer["name"],
        food=customer["food"]
    ) for customer in customers]

    cinema_hall_instance = CinemaHall(number=hall_number)
    cinema_bar_instance = CinemaBar()
    cleaning_staff_instance = Cleaner(name=cleaner)

    for customer_instance in customer_instances:
        cinema_bar_instance.sell_product(
            customer=customer_instance,
            product=customer_instance.food
        )

    cinema_hall_instance.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaning_staff_instance
    )
