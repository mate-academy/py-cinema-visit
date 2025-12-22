from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = []
    for customer in customers:
        customer_instances.append(
            Customer(customer["name"], customer["food"])
        )
    cinema_hall_instance = CinemaHall(hall_number)
    cinema_bar_instance = CinemaBar()
    cleaner_instance = Cleaner(cleaner)
    for customer in customer_instances:
        cinema_bar_instance.sell_product(customer.food, customer)
    cinema_hall_instance.movie_session(
        movie,
        customer_instances,
        cleaner_instance
    )
