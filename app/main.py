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
    customer_objs: List[Customer] = []
    for cust in customers:
        customer_instance = Customer(name=cust["name"], food=cust["food"])
        CinemaBar.sell_product(
            product=cust["food"],
            customer=customer_instance
        )
        customer_objs.append(customer_instance)

    cleaner_instance = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customer_objs,
        cleaning_staff=cleaner_instance
    )
