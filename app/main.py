from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    customer_objects = []
    for customer_dict in customers:
        customer_obj = Customer(customer_dict["name"], customer_dict["food"])
        CinemaBar.sell_product(customer_dict["food"], customer_obj)
        customer_objects.append(customer_obj)
    cinema_hall.movie_session(movie, customer_objects, cleaner_obj)
