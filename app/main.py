from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_instance = [Customer(customer.get("name"),
                                   customer.get("food"))
                          for customer in customers]

    for customer in customers_instance:
        CinemaBar.sell_product(customer, customer.food)
    CinemaHall(hall_number).movie_session(movie,
                                          customers_instance,
                                          Cleaner(cleaner))
