from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customers_instance = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]

    hall_instance = CinemaHall(hall_number)
    cinema_bar_instance = CinemaBar()
    cleaner_instance = Cleaner(cleaner)

    for customer in customers_instance:
        cinema_bar_instance.sell_product(customer, customer.food)

    hall_instance.movie_session(movie, customers_instance, cleaner_instance)
