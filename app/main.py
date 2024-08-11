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
    customers_in_movie = []
    hall = CinemaHall(hall_number)
    cleaner_stuff = Cleaner(cleaner)
    cinema_bar = CinemaBar()
    for customer in customers:
        customers_in_movie.append(Customer(customer["name"], customer["food"]))

    for customer_in_movie in customers_in_movie:
        cinema_bar.sell_product(customer_in_movie, customer_in_movie.food)

    hall.movie_session(movie, customers_in_movie, cleaner_stuff)
