from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_objs = []
    for customer in customers:
        customer_instance = (Customer(customer["name"], customer["food"]))
        customer_objs.append(customer_instance)
        CinemaBar.sell_product(customer_objs[-1].food, customer_instance)
    clean = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customer_objs, clean)
