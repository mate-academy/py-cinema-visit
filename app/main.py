from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str,
                 movie: str) -> None:
    customer_instance = []
    for customer in customers:
        cus = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(cus, customer["food"])
        customer_instance.append(cus)
    ch = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    ch.movie_session(movie_name=movie, customers=customer_instance,
                     cleaning_staff=clean)
