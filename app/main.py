from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict], hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_list = []

    for customer in customers:
        customer_inst = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer_inst, customer["food"])
        customers_list.append(customer_inst)

    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, customers_list, Cleaner(cleaner))
