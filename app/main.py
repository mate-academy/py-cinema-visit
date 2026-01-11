from bar import CinemaBar
from hall import CinemaHall
from people.customers import Customer
from people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:

    customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for customer in customers:
        CinemaBar.sell_product(customer.food, customer)
    cinema_hall.movie_session(movie, customers, cleaner)
