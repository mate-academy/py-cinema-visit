from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    hall_number = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    byers = []
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        byers.append(customer)
        CinemaBar.sell_product(customer, customer.food)
    CinemaHall.movie_session(hall_number, movie, byers, cleaner)
