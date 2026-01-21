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

    customers = [
        Customer(customer.get("name"), customer.get("food"))
        for customer in customers
    ]

    for customer in customers:
        CinemaBar.sell_product(customer, customer.food)

    cleaner = Cleaner(cleaner)

    CinemaHall(hall_number).movie_session(movie, customers, cleaner)
