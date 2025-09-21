# write your imports here
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    customers_objects = []
    for customer in customers:
        _customer = Customer(customer["name"], customer["food"])
        customers_objects.append(_customer)
        CinemaBar.sell_product(_customer, movie)
    hall.movie_session(movie, customers_objects, cleaner)