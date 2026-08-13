from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    customers_objects = []
    for customer in customers:
        customer_obj = Customer(customer["name"], customer["food"])
        customers_objects.append(customer_obj)
        CinemaBar.sell_product(customer["food"], customer_obj)

    hall.movie_session(movie, customers_objects, cleaning_staff)
