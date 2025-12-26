from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers = [Customer(customer.get("name"), customer.get("food"))
                 for customer in customers]
    cb = CinemaBar()
    for customer in customers:
        cb.sell_product(customer, customer.food)

    ch = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    ch.movie_session(movie, customers, cleaner)
