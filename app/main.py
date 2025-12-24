from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers_info: List[Dict[str, str]],
        hall_number: int,
        cleaner_name: str,
        movie: str
) -> None:
    customers = [
        Customer(name=customer["name"],
                 food=customer["food"])
        for customer in customers_info
    ]

    for customer in customers:
        CinemaBar.sell_product(customer.food, customer)
    CinemaHall(hall_number).movie_session(
        movie,
        customers,
        Cleaner(cleaner_name)
    )
