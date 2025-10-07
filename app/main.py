from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    one_customer = []

    for i in range(len(customers)):
        one_customer.append(
            Customer(customers[i]["name"], customers[i]["food"])
        )
        CinemaBar.sell_product(one_customer[i].food, one_customer[i])

    CinemaHall(hall_number).movie_session(
        movie, one_customer, Cleaner(cleaner)
    )
