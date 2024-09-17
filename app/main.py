from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner_name: str,
        movie: str
) -> None:
    bar_instance = CinemaBar()
    hall_instance = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner_name)
    customer_instances = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for customer_instance in customer_instances:
        bar_instance.sell_product(
            customer_instance.name, customer_instance.food
        )

    hall_instance.movie_session(movie, customer_instances, cleaner_instance)
