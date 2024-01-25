from typing import List
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
# write your imports here


def cinema_visit(customers: List[dict],
                 hall_number: int,
                 cleaning_staff: str,
                 movie_name: str,) -> None:
    customers = [Customer(data["name"], data["food"]) for data in customers]
    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    clean = Cleaner(cleaning_staff)
    for cust in customers:
        cinema_bar.sell_product(cust.food, cust)
    hall.movie_session(movie_name, customers, clean)
