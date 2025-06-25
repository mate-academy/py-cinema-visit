from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict[str, str]],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    actual_customers: list[Customer] = []
    for customer in customers:
        actual_customer = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(actual_customer.food, actual_customer)
        actual_customers.append(actual_customer)
    CinemaHall(
        hall_number).movie_session(movie, actual_customers, Cleaner(cleaner))
