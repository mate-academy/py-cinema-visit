from typing import List

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: List[dict[str, str]],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    hall_customers = [Customer(customer["name"],
                      customer["food"])
                      for customer in customers]

    hall = CinemaHall(hall_number=hall_number)
    hall_cleaner = Cleaner(name=cleaner)
    for customer in hall_customers:
        CinemaBar.sell_product(customer.food, customer)
    hall.movie_session(movie, hall_customers, hall_cleaner)
