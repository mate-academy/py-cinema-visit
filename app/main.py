from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(movie: str, customers: list, hall_number: int, cleaner: str):

    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    customers_objects = []

    for customer in customers:
        customer.obj = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(product=customer["food"], customer=customer.obj)
        customers_objects.append(customer.obj)

    cinema_hall.movie_session(movie_name=movie, customers=customers_objects, cleaning_staff=cleaning_staff)
