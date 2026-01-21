from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    for cust in customers:
        customer = Customer(cust["name"], cust["food"])
        cb = CinemaBar
        cb.sell_product(cust["food"], customer)
    ch = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    ch.movie_session(movie, customers, cleaner_obj)
