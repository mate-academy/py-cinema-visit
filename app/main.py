from typing import List, Dict

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customer_objs: List[Customer] = []
    for customer_data in customers:
        customer_obj = Customer(
            name=customer_data["name"],
            food=customer_data["food"],
        )
        CinemaBar.sell_product(
            product=customer_obj.food,
            customer=customer_obj,
        )
        customer_objs.append(customer_obj)

    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=customer_objs,
        cleaning_staff=cleaning_staff,
    )
