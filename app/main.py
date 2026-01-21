from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_classes = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for customer in customers_classes:
        CinemaBar.sell_product(customer.food, customer)

    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customers_classes, Cleaner(cleaner))
