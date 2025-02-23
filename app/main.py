from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    customer_instances = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]

    cleaner_instance = Cleaner(cleaner)
    hall_instance = CinemaHall(hall_number)

    for customer in customer_instances:
        CinemaBar.sell_product(customer, customer.food)

    hall_instance.movie_session(movie, customer_instances, cleaner_instance)
