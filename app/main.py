from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(movie: str,
                 customers: list,
                 hall_number: int,
                 cleaner: str) -> None:
    customer_objects = []
    for customer in customers:
        customer_instance = Customer(customer["name"], customer["food"])
        customer_objects.append(customer_instance)
    for customer_instance in customer_objects:
        CinemaBar.sell_product(customer_instance.food, customer_instance)
    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)
    hall.movie_session(movie, customer_objects, cleaning_staff)
