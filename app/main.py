from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from typing import List, Dict


def cinema_visit(customers: List[Dict[str, str]],
                 hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_instances = []
    for customer_info in customers:
        customer = Customer(name=customer_info["name"],
                            food=customer_info["food"])
        customer_instances.append(customer)

    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food,
                               customer=customer)

    hall = CinemaHall(number=hall_number)

    hall.movie_session(movie_name=movie,
                       customers=customer_instances,
                       cleaning_staff=Cleaner(name=cleaner))
