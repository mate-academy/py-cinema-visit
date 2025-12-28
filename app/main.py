from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    """
    Simulates a cinema visit: customers buy food,
    watch a movie, and the hall is cleaned.

    :param customers: List of customer data,
    where each item is a dict with 'name' and 'food' keys.
    :param hall_number: The number of the cinema hall.
    :param cleaner: The name of the cleaner responsible
    for cleaning after the session.
    :param movie: The title of the movie being shown.
    """
    customers_object = [Customer(name=c["name"],
                                 food=c["food"]) for c in customers]
    cleaner_current = Cleaner(name=cleaner)

    for customer in customers_object:
        CinemaBar.sell_product(product=customer.food
                               , customer=customer)

    hall_current = CinemaHall(number=hall_number)
    hall_current.movie_session(movie_name=movie,
                               customers=customers_object,
                               cleaning_staff=cleaner_current)
