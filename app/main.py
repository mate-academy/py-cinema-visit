from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers = Customer(customers)
    cleaner = Cleaner(cleaner)
    bar = CinemaBar()
    hall = CinemaHall(hall_number)
    bar.sell_product(customers, movie)
    hall.movie_session(movie, customers, cleaner)
