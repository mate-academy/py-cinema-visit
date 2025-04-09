from cinema.bar import CinemaBar
from cinema.hall import CinemaHall
from people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str)\
        -> None:
    bar_cinema = CinemaBar()
    hall = CinemaHall(hall_number)
    for customer in customers:
        bar_cinema.sell_product(customer, customer["food"])
    hall.movie_session(movie, customers, Cleaner(cleaner))
