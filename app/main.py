from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(hall_number: int, cleaner: str, movie: str, customers: list):

    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    customers_objects = []
    for customer in customers:
        customer_obj = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(product=customer["food"], customer=customer_obj)
        customers_objects.append(customer_obj)


    cinema_hall.movie_session(movie_name=movie, customers=customers_objects, cleaning_staff=cleaning_staff)