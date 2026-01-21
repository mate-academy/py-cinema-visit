from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_instance = []

    for customer in customers:
        customer_ = Customer(
            customer.get("name"),
            customer.get("food")
        )
        customers_instance.append(customer_)
        CinemaBar.sell_product(customer_, customer_.food)

    CinemaHall(hall_number).movie_session(
        movie,
        customers_instance,
        Cleaner(cleaner)
    )
