from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(movie: str,
                 customers: list[dict],
                 hall_number: int,
                 cleaner: str) -> None:
    result = []
    for customer in customers:
        result.append(Customer(customer["food"], customer["name"]))
    for customer in result:
        CinemaBar.sell_product(customer.food, customer)

    CinemaHall(hall_number).movie_session(movie, result, Cleaner(cleaner))
