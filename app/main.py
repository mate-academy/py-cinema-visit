from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: List[Dict[str, str]], hall_number: int, cleaner: str, movie: str
) -> None:

    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    cinema_bar = CinemaBar()
    customers_in_hall = [
        Customer(
            customer.get("name"),
            customer.get("food")
        )
        for customer in customers
    ]

    for customer in customers_in_hall:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customers_in_hall, cleaner_instance)
