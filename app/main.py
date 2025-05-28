from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    customers = [Customer(**data) for data in customers]
    cleaner = Cleaner(cleaner)
    bar = CinemaBar()
    hall = CinemaHall(hall_number)
    for customer in customers:
        bar.sell_product(customer, movie)
    hall.movie_session(movie, customers, cleaner)
