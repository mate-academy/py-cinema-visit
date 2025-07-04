from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str,
                 movie: str) -> object:
    for human in customers:

        make = Customer(human["name"], human["food"])

        CinemaBar.sell_product(make, make.food)

    numb = CinemaHall(hall_number)
    customer_objects = [Customer(c["name"], c["food"]) for c in customers]
    return numb.movie_session(movie, customer_objects, Cleaner(cleaner))
