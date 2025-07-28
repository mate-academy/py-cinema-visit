from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_objects = []
    for customer in customers:
        person = Customer(name=customer["name"], food=customer["food"])
        CinemaBar.sell_product(customer["food"], person)
        customer_objects.append(person)

    cleaner_obj = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customer_objects, cleaner_obj)
