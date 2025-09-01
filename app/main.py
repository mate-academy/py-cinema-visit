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
    customer_objects: List[Customer] = []

    for customer_data in customers:
        cust = Customer(name=customer_data["name"], food=customer_data["food"])
        CinemaBar.sell_product(product=cust.food, customer=cust)
        customer_objects.append(cust)

    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    hall.movie_session(movie_name=movie,
                       customers=customer_objects,
                       cleaning_staff=cleaning_staff)
