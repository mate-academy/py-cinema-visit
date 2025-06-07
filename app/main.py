from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_objects = []

    for customer in customers:
        customer_obj = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer_obj, customer_obj.food)
        customer_objects.append(customer_obj)

    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    hall.movie_session(movie, customer_objects, cleaner_obj)
