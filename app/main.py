from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)

    customer_instances = [Customer(customer["name"], customer["food"])
                          for customer in customers]
    for customer in customer_instances:
        cinema_bar.sell_product(customer, customer.food)

    cleaner_instance = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customer_instances, cleaner_instance)
