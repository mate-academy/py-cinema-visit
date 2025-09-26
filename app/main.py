from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(movie: str, customers: list, hall_number: int, cleaner: str)\
        -> None:
    ch = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    for u in customers:
        Customer(u["name"], u["food"])
    for customer in customers:
        CinemaBar.sell_product(customer.name, customer.food)
    ch.movie_session(movie_name=movie, customers=customers, cleaning_staff=clean)