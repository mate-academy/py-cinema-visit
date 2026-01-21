from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    customers_instances = []
    for customer in customers:
        customers_instances.append(
            Customer(customer["name"], customer["food"]))

    hall_number_instances = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_instances = Cleaner(cleaner)

    for customer in customers_instances:
        cinema_bar.sell_product(product=customer.food, customer=customer)
    hall_number_instances.movie_session(
        movie,
        customers_instances,
        cleaner_instances)
