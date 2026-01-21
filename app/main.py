from __future__ import annotations
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_list = [Customer(name=i["name"], food=i["food"])
                     for i in customers]
    hall_numb = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_name = Cleaner(cleaner)
    for customer in customer_list:
        cinema_bar.sell_product(customer.food, customer)
    hall_numb.movie_session(movie, customer_list, cleaner_name)
