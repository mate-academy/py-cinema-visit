from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie_name: str) -> None:
    customer_instances = []

    for customer in customers:
        instance = Customer(customer["name"], customer["food"])
        customer_instances.append(instance)

    hall = CinemaHall(hall_number)
    stuff = Cleaner(cleaner)
    cinema_bar = CinemaBar()

    for customer in customer_instances:
        cinema_bar.sell_product(customer.food, customer)

    hall.movie_session(movie_name, customer_instances, stuff)
