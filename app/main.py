from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    hall = CinemaHall(hall_number)
    bar = CinemaBar()

    formatted_customers = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    formatted_cleaner = Cleaner(cleaner)

    for customer in formatted_customers:
        bar.sell_product(customer, customer.food)

    hall.movie_session(movie, formatted_customers, formatted_cleaner)
