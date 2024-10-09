from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    list_of_customer_instances = []
    for customer in customers:
        list_of_customer_instances.append(
            Customer(customer["name"], customer["food"])
        )

    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_staff = Cleaner(cleaner)
    for customer_instance in list_of_customer_instances:
        cinema_bar.sell_product(customer_instance.food, customer_instance)

    hall.movie_session(movie, list_of_customer_instances, cleaner_staff)
