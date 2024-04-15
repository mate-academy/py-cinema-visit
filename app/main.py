from typing import List, Dict

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: List[Dict[str, str]],
                 hall_number: int,
                 cleaner_name: str,
                 movie: str) -> None:
    cinema_hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner_name)

    customer_list = []

    for customer_data in customers:
        customer = Customer(name=customer_data["name"],
                            food=customer_data["food"])
        CinemaBar.sell_product(customer, customer.food)
        customer_list.append(customer)

    cinema_hall.movie_session(movie_name=movie,
                              customers=customer_list,
                              cleaning_staff=cleaner_instance)
