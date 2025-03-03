from typing import Any
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> Any:
    list_of_customers = [
        Customer(dic["name"], dic["food"]) for dic in customers
    ]
    hall = CinemaHall(hall_number)
    cleanman = Cleaner(cleaner)
    for custom in list_of_customers:
        CinemaBar.sell_product(custom, custom.food)
    hall.movie_session(movie, list_of_customers, cleanman)
