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
    cleaner_instance = Cleaner(cleaner)
    cinema_instance = CinemaHall(hall_number)
    customer_instances = []
    for i in customers:
        customer_instance = Customer(i["name"], i["food"])
        CinemaBar.sell_product(i["food"], customer_instance)
        customer_instances.append(customer_instance)
    cinema_instance.movie_session(movie, customer_instances, cleaner_instance)
