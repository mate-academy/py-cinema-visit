from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_instances = [Customer(data["name"],
                                   data["food"]) for data in customers]
    cinema_bar = CinemaBar()
    for customer_instance in customer_instances:
        cinema_bar.sell_product(customer_instance, customer_instance.food)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, customer_instances, Cleaner(cleaner))
