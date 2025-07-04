from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str,
                 movie: str) -> object:
    for human in customers:

        make = Customer(human["name"], human["food"])

        CinemaBar.sell_product(make.name, make.food)

    numb = CinemaHall(hall_number)
    return numb.movie_session(movie, customers, Cleaner(cleaner))
