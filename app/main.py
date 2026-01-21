from typing import List, Dict
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_objects = [
        Customer(name=c["name"], food=c["food"])
        for c in customers
    ]

    cleaning_staff = Cleaner(name=cleaner)

    for cust in customer_objects:
        CinemaBar.sell_product(product=cust.food, customer=cust)

    hall = CinemaHall(number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
