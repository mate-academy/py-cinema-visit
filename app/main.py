from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_obj = []

    for person in customers:
        customer = Customer(person["name"],
                            person["food"])
        CinemaBar.sell_product(customer.food, customer)
        customer_obj.append(customer)
    CinemaHall(hall_number).movie_session(movie,
                                          customer_obj,
                                          Cleaner(cleaner))
