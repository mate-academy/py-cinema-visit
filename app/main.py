from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> str:
    new_customers = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]

    for customer in new_customers:
        CinemaBar.sell_product(customer, customer.food)

    hall_cleaner = Cleaner(cleaner)
    session = CinemaHall(hall_number)
    session.movie_session(movie, new_customers, hall_cleaner)
