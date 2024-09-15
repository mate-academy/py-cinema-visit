from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from typing import List


def cinema_visit(
        customers: List[dict],
        hall_number: int,
        cleaning_staff: str,
        movie_name: str) -> None:

    customers_instances = []
    for customer in customers:
        customer_instance = Customer(customer["name"], customer["food"])
        customers_instances.append(customer_instance)

    hall = CinemaHall(hall_number)
    bar_clients = CinemaBar()
    cleaner = Cleaner(cleaning_staff)

    for person in customers_instances:
        bar_clients.sell_product(customer=person, product=person.food)

    hall.movie_session(movie_name, customers_instances, cleaner)
