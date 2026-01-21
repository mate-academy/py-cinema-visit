from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from typing import List


def cinema_visit(
        customers: List["Customer"],
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:
    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaning_staff)
    customers_instances = []

    for cust in customers:
        customer = Customer(cust["name"], cust["food"])
        customers_instances.append(customer)
        cinema_bar.sell_product(customer.food, customer)

    hall.movie_session(movie_name, customers_instances, cleaner_instance)
