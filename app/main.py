from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaning_staff: str,
                 movie_name: str) -> None:
    customers = [
        Customer(customer.get("name"), customer.get("food"))
        for customer in customers
    ]

    for visitor in customers:
        CinemaBar.sell_product(visitor.food, visitor)

    cleaner = Cleaner(cleaning_staff)
    CinemaHall(hall_number).movie_session(movie_name, customers, cleaner)
