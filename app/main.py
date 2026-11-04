from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cleaner = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    customers_objs = []
    for customer in customers:
        customers_obj = Customer(customer["name"], customer["food"])
        customers_objs.append(customers_obj)
        CinemaBar.sell_product(customers_obj, customer["food"])
    cinema_hall.movie_session(movie, customers_objs, cleaner)
