from cinema.bar import CinemaBar
from cinema.hall import CinemaHall
from people.customer import Customer
from people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_inst = CinemaHall(hall_number)
    cleaner_inst = Cleaner(cleaner)
    customer_list = []
    for customer in customers:
        customer_inst = Customer(customer["name"], customer["food"])
        customer_list.append(customer_inst)
        CinemaBar.sell_product(customer["food"], customer_inst)
    cinema_inst.movie_session(movie, customer_list, cleaner_inst)
