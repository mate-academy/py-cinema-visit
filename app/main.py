from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_instances = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    cinema_hall_instance = CinemaHall(hall_number)

    cleaner_instance = Cleaner(cleaner)

    for customer_instance in customers_instances:
        CinemaBar.sell_product(customer_instance.food, customer_instance)

    cinema_hall_instance.movie_session(
        movie,
        customers_instances,
        cleaner_instance
    )
