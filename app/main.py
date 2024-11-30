from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_instances = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    for customer in customers_instances:
        CinemaBar.sell_product(customer=customer, product=customer.food)
    CinemaHall(hall_number).movie_session(movie, customers_instances, Cleaner(cleaner))
