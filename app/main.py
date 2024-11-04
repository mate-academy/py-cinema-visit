from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    customer_instances = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    hall_instance = CinemaHall(hall_number)
    bar_instance = CinemaBar()
    cleaner_instance = Cleaner(cleaner)

    [
        bar_instance.sell_product(customer, customer.food)
        for customer in customer_instances
    ]
    hall_instance.movie_session(movie, customer_instances, cleaner_instance)
