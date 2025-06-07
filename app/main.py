from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:

    customer_instances = []
    for customer in customers:
        customer_obj = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer["food"], customer_obj)
        customer_instances.append(customer_obj)

    hall_obj = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    hall_obj.movie_session(movie, customer_instances, cleaner_obj)
