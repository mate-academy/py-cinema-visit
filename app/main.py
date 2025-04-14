from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: List[Dict[str, str]], hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_objects = [Customer(customer_data["name"], customer_data["food"])
                        for customer_data in customers]
    cleaner_object = Cleaner(cleaner)

    cinema_bar_instance = CinemaBar()
    for customer in customer_objects:
        cinema_bar_instance.sell_product(customer.food, customer)

    hall = CinemaHall(hall_number)
    hall.movie_session(movie_name=movie, customers=customer_objects,
                       cleaning_staff=cleaner_object)
