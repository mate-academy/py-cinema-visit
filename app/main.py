from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):

    hall = CinemaHall(hall_number)
    bar = CinemaBar()

    ready_customers = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]

    ready_cleaner = Cleaner(cleaner)

    for customer in ready_customers:
        bar.sell_product(customer, customer.food)

    hall.movie_session(movie, ready_customers, ready_cleaner)
