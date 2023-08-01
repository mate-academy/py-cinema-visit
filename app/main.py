from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cleaner_obj = Cleaner(cleaner)
    customers_obj = []

    for cinema_customer in customers:
        customer = Customer(cinema_customer["name"], cinema_customer["food"])
        customers_obj.append(customer)
        CinemaBar.sell_product(customer, customer.food)

    CinemaHall(hall_number).movie_session(movie,
                                          customers_obj,
                                          cleaner_obj)
