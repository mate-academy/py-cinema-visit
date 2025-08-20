from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_from_dicts = [Customer(**customer) for customer in customers]
    for customer in customers_from_dicts:
        CinemaBar.sell_product(customer.food, customer)
    CinemaHall(hall_number).movie_session(
        movie,
        customers_from_dicts,
        Cleaner(cleaner)
    )
