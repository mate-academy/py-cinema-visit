from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> str:
    customer_instances = []
    cinema_bar = CinemaBar()
    for customer in customers:
        customer_instance = Customer(customer["name"], customer["food"])
        customer_instances.append(customer_instance)
        cinema_bar.sell_product(customer["food"], customer_instance)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, customer_instances, Cleaner(cleaner))
    return f"{cinema_bar} {cinema_hall} {customer_instances}"
