from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[Customer], hall_number: int, cleaner: str,
                 movie: str) -> None:
    staff = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    customers_new = []
    for customer_dict in customers:
        customer = Customer(customer_dict["name"], customer_dict["food"])
        CinemaBar.sell_product(customer, customer_dict["food"])
        customers_new.append(customer)
    hall.movie_session(movie, customers_new, staff)
