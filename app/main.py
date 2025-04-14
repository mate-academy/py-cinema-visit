from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from typing import List, Dict


def cinema_visit(
        customers: List[Dict[str, str]],
        number: int,
        cleaner: str,
        movie: str
) -> None:
    cleaner_instance = Cleaner(name=cleaner)
    hall_instance = CinemaHall(number=number)

    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        CinemaBar.sell_product(
            customer.food,
            customer
        )

    hall_instance.movie_session(
        movie_name=movie,
        customers=[
            Customer(
                name=c["name"],
                food=c["food"]
            ) for c in customers
        ],
        cleaner=cleaner_instance
    )
