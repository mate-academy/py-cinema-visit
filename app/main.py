from typing import List

from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: List[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_bar_instance = CinemaBar()
    cinema_hall_instance = CinemaHall(number=hall_number)
    cleaning_staff_instance = Cleaner(name=cleaner)

    customer_instances = [Customer(
        name=customer_data["name"],
        food=customer_data["food"]
    ) for customer_data in customers]

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
