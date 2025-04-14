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
    customer_object = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]

    for customer in customer_object:
        CinemaBar.sell_product(customer, customer.food)

    CinemaHall.movie_session(
        CinemaHall(hall_number),
        movie, customer_object,
        Cleaner(cleaner)
    )
