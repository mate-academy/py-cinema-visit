from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    list_customer_instance = []
    for cust_r in customers:
        customer = Customer(cust_r["name"], cust_r["food"])
        list_customer_instance.append(customer)
        CinemaBar.sell_product(customer, cust_r["food"])
    CinemaHall(hall_number).movie_session(movie,
                                          list_customer_instance,
                                          Cleaner(cleaner))
