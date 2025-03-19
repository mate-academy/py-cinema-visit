from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers_list = []
    for customer in customers:
        customer_info = Customer(customer["name"], customer["food"])
        customers_list.append(customer_info)
        CinemaBar.sell_product(customer["food"], customer_info)

    movie_info = (movie, customers_list, Cleaner(cleaner))
    CinemaHall(hall_number).movie_session(*movie_info)
