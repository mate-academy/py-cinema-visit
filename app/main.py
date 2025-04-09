from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str)\
        -> None:
    bar_cinema = CinemaBar()
    hall = CinemaHall(hall_number)
    customers_class = [Customer(customer["name"], customer["food"]) for customer in customers]
    for customer in customers_class:
        bar_cinema.sell_product(customer, customer.food)
    hall.movie_session(movie, customers_class, Cleaner(cleaner))
