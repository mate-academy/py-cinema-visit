from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaning_staff: str, movie_name: str) -> None:
    cinema_bar = CinemaBar()
    customer_instances = []
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        customer_instances.append(new_customer)
        cinema_bar.sell_product(customer["food"], new_customer)
    CinemaHall(hall_number).movie_session(
        movie_name, customer_instances, Cleaner(cleaning_staff))
