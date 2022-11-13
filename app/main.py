from typing import Callable

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> Callable:
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    list_of_customers = []
    for person in customers:
        customer = Customer(person["name"], person["food"])
        CinemaBar.sell_product(customer, customer.food)
        list_of_customers.append(customer)
    hall.movie_session(movie, list_of_customers, cleaner)

# customers = [
#     {"name": "Bob", "food": "Coca-cola"},
#     {"name": "Alex", "food": "popcorn"}
# ]
# cinema_visit(customers=customers, hall_number=5,
# cleaner="Anna", movie="Madagascar")
