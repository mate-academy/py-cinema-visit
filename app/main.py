from __future__ import annotations
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict], 
        hall_number: int, 
        cleaner: str, 
        movie: str
    ) -> None:

    current_customers = []
    current_hall = CinemaHall(hall_number)
    current_cleaner = Cleaner(cleaner)

    for customer in customers:
        current_customers.append(Customer(customer["name"], customer["food"]))

    for customer in current_customers:
        CinemaBar.sell_product(customer, customer.food)

    current_hall.movie_session(movie, current_customers, current_cleaner)
