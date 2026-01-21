from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers_list = []
    for customer in customers:
        customer_obj = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer["food"], customer_obj)
        customers_list.append(customer_obj)

    CinemaHall(hall_number).movie_session(movie,
                                          customers_list,
                                          Cleaner(cleaner))
