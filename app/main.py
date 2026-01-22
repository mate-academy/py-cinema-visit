from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    bar_ = CinemaBar()
    cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    customers_list = []
    for customer_ in customers:
        customer_ = Customer(customer_["name"], customer_["food"])
        bar_.sell_product(customer_.food, customer_)
        customers_list.append(customer_)

    hall.movie_session(movie, customers_list, cleaner)
