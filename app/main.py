from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaning_staff: str,
                 movie_name: str) -> None:
    customers = [
        Customer(customer.get("name"), customer.get("food"))
        for customer in customers
    ]
    for customer in customers:
        CinemaBar.sell_product(customer.food, customer)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie_name, customers, Cleaner(cleaning_staff))
