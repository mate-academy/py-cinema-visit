from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    hall_number = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    customer_list = []
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer.food, customer)
        customer_list.append(customer)
    CinemaHall.movie_session(hall_number, movie, customer_list, cleaner)
