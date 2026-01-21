from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall as CHall

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    new_customers = []
    for customer in customers:
        customer = Customer(**customer)
        CinemaBar().sell_product(customer, customer.food)
        new_customers.append(customer)
    CHall(hall_number).movie_session(movie, new_customers, Cleaner(cleaner))
