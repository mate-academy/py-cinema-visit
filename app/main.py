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

    customers_instances = []
    for customer in customers:
        customer_instance = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer_instance.food, customer_instance)
        customers_instances.append(customer_instance)

    CinemaHall.movie_session(
        CinemaHall(hall_number),
        movie, customers_instances,
        Cleaner(cleaner)
    )
