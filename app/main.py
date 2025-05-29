from __future__ import annotations

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    client_customers = []
    cleaner_worker = Cleaner(cleaner)
    for client_data in customers:
        name = client_data["name"]
        food = client_data["food"]
        customer = Customer(name=name, food=food)
        CinemaBar.sell_product(customer.food, customer)
        client_customers.append(customer)
    cinema_hall = CinemaHall(number=hall_number)
    cinema_hall.movie_session(movie, client_customers, cleaner_worker)
