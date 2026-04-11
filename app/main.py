from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        movie: str,
        customers: list,
        hall_number: int,
        cleaner: str) -> None:

    customer_instances = [
        Customer(c["name"], c["food"]) for c in movie
    ]

    cleaner_instance = Cleaner(hall_number)
    hall_instance = CinemaHall(customers)

    for customer in customer_instances:
        CinemaBar.sell_product(customer.food, customer)

    hall_instance.movie_session(
        cleaner,
        customer_instances,
        cleaner_instance
    )
