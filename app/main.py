from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers_list: list[dict[str, str]],
        hall_id: int,
        cleaner_name: str,
        movie_title: str
) -> None:
    customer_instances = [
        Customer(customer["name"], customer["food"])
        for customer in customers_list
    ]
    cinema_hall = CinemaHall(hall_id)
    cinema_bar = CinemaBar()
    cleaner_instance = Cleaner(cleaner_name)
    for customer in customer_instances:
        cinema_bar.sell_product(customer, customer.food)
    cinema_hall.movie_session(
        movie_title,
        customer_instances,
        cleaner_instance
    )
