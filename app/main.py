from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner_name: str, movie: str) -> None:
    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    customer_instances = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    cleaner_instance = Cleaner(cleaner_name)
    for customer in customer_instances:
        cinema_bar.sell_product(customer, customer.food)
    hall.movie_session(movie, customer_instances, cleaner_instance)
