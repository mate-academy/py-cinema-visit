from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
        movie: str,
        customers: list,
        hall_number: int,
        cleaner: str
) -> None:
    cust_list = []
    for customer in customers:
        customer_instance = Customer(**customer)
        CinemaBar.sell_product(customer_instance.food, customer_instance)
        cust_list.append(customer_instance)
    hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    hall.movie_session(movie, cust_list, clean)

