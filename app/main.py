from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_list = []
    for customer in customers:
        current_customer = Customer(customer["name"], customer["food"])
        customer_list.append(current_customer)
        CinemaBar.sell_product(customer["food"], current_customer)

    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    cinema_hall.movie_session(movie, customer_list, cleaner)
