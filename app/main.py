from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner


def create_customer_instances(customers: list[dict]) -> list[Customer]:
    return [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]


def perform_cinema_visit(customer_instances: list[Customer],
                         hall_number: int,
                         cleaning_staff: str,
                         movie_name: str) -> None:
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_instance = Cleaner(cleaning_staff)

    for customer in customer_instances:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie_name, customer_instances, cleaner_instance)


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaning_staff: str,
                 movie_name: str) -> None:
    customer_instances = create_customer_instances(customers)
    perform_cinema_visit(
        customer_instances, hall_number, cleaning_staff, movie_name
    )
