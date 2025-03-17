from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_line = []

    cinema_hall = CinemaHall(hall_number)
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        customer_line.append(customer)

    bar = CinemaBar()
    for customer in customer_line:
        bar.sell_product(customer, customer.food)

    service = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customer_line, service)
