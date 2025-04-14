from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict], hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_list = []
    cinema_hall = CinemaHall(hall_number)
    for customer in customers:
        customer_obj = Customer(customer["name"], customer["food"])
        customer_list.append(customer_obj)
        CinemaBar.sell_product(customer_obj, customer_obj.food)
    cinema_hall.movie_session(movie, customer_list, Cleaner(cleaner))
