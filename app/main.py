from typing import List
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: List[dict], hall_number: int, cleaner: str, movie: str):
    # cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)
    cinema_customers = [Customer(customer.get("name"), customer.get("food")) for customer in customers]

    for cinema_customer in cinema_customers:
        CinemaBar.sell_product(cinema_customer.food, cinema_customer)

    cinema_hall.movie_session(movie, cinema_customers, cinema_cleaner)
