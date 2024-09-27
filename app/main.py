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
    cinema_customers = [Customer(**customer) for customer in customers]
    for cinema_customer in cinema_customers:
        CinemaBar.sell_product(cinema_customer.food, cinema_customer)
    CinemaHall(hall_number).movie_session(
        movie, cinema_customers, Cleaner(cleaner)
    )
