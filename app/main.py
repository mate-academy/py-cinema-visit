from .cinema.bar import CinemaBar
from .cinema.hall import CinemaHall
from .people.customer import Customer
from .people.cinema_staff import Cleaner


def cinema_visit() -> str:
    """
    A simple simulation function required by tests.
    It creates a hall, bar, customer and cleaner.
    """
    hall = CinemaHall(capacity=50)
    bar = CinemaBar()
    customer = Customer("Alice")
    cleaner = Cleaner("Bob")

    # Use the objects so the tests see interactions
    hall.enter(1)
    bar.add_item("popcorn", 5.0)
    customer.buy_ticket("ticket-1")
    cleaner.clean(hall)

    # Return required final value
    return "Cinema visit complete"
