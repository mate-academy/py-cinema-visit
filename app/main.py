from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:

    customer_objects = [Customer(c["name"], c["food"]) for c in customers]
    hall_instance = CinemaHall(hall_number)
    cleaner_object = Cleaner(cleaner)

    for customer_obj in customer_objects:
        CinemaBar.sell_product(customer_obj.food, customer_obj)

    hall_instance.movie_session(movie, customer_objects, cleaner_object)
