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
    customer_objects = [Customer(c["name"], c["food"]) for c in customers]

    for customer in customer_objects:
        CinemaBar.sell_product(customer, customer.food)

    CinemaHall(hall_number).movie_session(
        movie,
        customer_objects,
        Cleaner(cleaner)
    )
