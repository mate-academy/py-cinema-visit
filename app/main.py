from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cust = []
    for customer in customers:
        cust_inst = Customer(**customer)
        CinemaBar.sell_product(cust_inst.food, cust_inst)
        cust.append(cust_inst)

    cln = Cleaner(cleaner)
    CinemaHall(hall_number).movie_session(movie, cust, cln)
