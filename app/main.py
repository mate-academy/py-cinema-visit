from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_list = []
    for customer in customers:
        customer_object = Customer(customer["name"], customer["food"])
        customers_list.append(customer_object)
        CinemaBar.sell_product(customer["food"],
                               customer_object)
    CinemaHall(hall_number).movie_session(movie_name=movie,
                                          customers=customers_list,
                                          cleaning_staff=Cleaner(cleaner))
