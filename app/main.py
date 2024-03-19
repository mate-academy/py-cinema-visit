from __future__ import annotations
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
app_path = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(app_path)


from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customers_list = []
    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_staff = Cleaner(cleaner)
    for customer_info in customers:
        customer = Customer(customer_info["name"], customer_info["food"])

        customers_list.append(customer)
        cinema_bar.sell_product(customer, customer.food)

    hall.movie_session(movie, customers_list, cleaner_staff)

print()
customers = [
{"name": "Susan", "food": "Pepsi"},
{"name": "Michael", "food": "Coca-cola"},
{"name": "Monica", "food": "popcorn"}
]
hall = 3
cleaner = "Vasiliy"
movie = "Interstellar"

cinema_visit(customers, hall, cleaner, movie)
