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
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_instance = Cleaner(cleaner)
    customer_instances = []

    for customer_info in customers:
        customer = Customer(customer_info["name"], customer_info["food"])
        customer_instances.append(customer)
        cinema_bar.sell_product(customer_info["food"], customer)

    cinema_hall.movie_session(movie, customer_instances, cleaner_instance)
