# write your imports here
from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(movie: str,
                 customers: List[Dict[str, str]],
                 hall_number: int,
                 cleaner: str) -> None:
    customer_objects = []

    for customer_data in customers:
        cust = Customer(name=customer_data["name"], food=customer_data["food"])
        customer_objects.append(cust)
        CinemaBar.sell_product(product=cust.food, customer=cust)

    hall = CinemaHall(number=hall_number)

    cleaner_obj = Cleaner(name=cleaner)

    hall.movie_session(movie_name=movie,
                       customers=customer_objects,
                       cleaning_staff=cleaner_obj)
