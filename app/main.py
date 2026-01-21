from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_list = []
    our_cleaner = Cleaner(cleaner)
    our_bar = CinemaBar()
    for visitor in customers:
        customer = Customer(visitor["name"], visitor["food"])
        customers_list.append(customer)
        our_bar.sell_product(customer, visitor["food"])
    CinemaHall(hall_number).movie_session(movie, customers_list, our_cleaner)
