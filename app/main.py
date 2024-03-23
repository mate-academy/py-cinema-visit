from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: List[Dict[str, str]],
                 hall_number: int,
                 cleaner_name: str,
                 movie: str) -> None:

    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner_name)

    for customer_data in customers:
        customer = Customer(name=customer_data["name"],
                            food=customer_data["food"])

        cinema_bar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie_name=movie,
                              customers=[Customer
                                         (name=customer_data["name"],
                                          food=customer_data["food"])
                                         for customer_data in customers],
                              cleaning_staff=cleaner_instance)
