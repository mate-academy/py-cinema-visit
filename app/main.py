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
    customer_instances = []
    for customer in customers:
        customer_instance = Customer(customer["name"], customer["food"])
        customer_instances.append(customer_instance)
    ch = CinemaHall(hall_number)
    cb = CinemaBar()
    cleaner = Cleaner(cleaner)

    for customer in customer_instances:
        cb.sell_product(customer, customer.food)
    ch.movie_session(movie, customer_instances, cleaner)
