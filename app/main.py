from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    instances = []
    cb = CinemaBar()
    for customer in customers:
        cust = Customer(customer["name"], customer["food"])
        instances.append(cust)
        cb.sell_product(cust.food, cust)
    ch = CinemaHall(hall_number)
    cl = Cleaner(cleaner)
    ch.movie_session(movie, instances, cl)
