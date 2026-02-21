from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    result = []
    for customer in customers:
        result.append(Customer(customer["name"], customer["food"]))
    for customer in result:
        CinemaBar.sell_product(customer, customer.food)

    CinemaHall(hall_number).movie_session(movie, result, Cleaner(cleaner))
