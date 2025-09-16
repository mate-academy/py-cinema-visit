from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    movie: str,
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
) -> None:
    customer_objs: List[Customer] = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]

    for customer in customer_objs:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objs,
        cleaning_staff=cleaning_staff,
    )
