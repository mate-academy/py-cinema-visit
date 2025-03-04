from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict[str, str]],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    """Simulates a cinema visit.

    This function creates customers, a cinema hall, and a cleaner,
    and then simulates a movie session.

    :param customers: A list of dictionaries,
        where each dictionary represents a customer.
    :type customers: list[dict[str, str]]
    :param hall_number: The number of the cinema hall.
    :type hall_number: int
    :param cleaner: The name of the cleaner.
    :type cleaner: str
    :param movie: The name of the movie.
    :type movie: str
    """
    customers_list = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for customer in customers_list:
        CinemaBar.sell_product(customer, customer.food)

    hall.movie_session(movie, customers_list, cleaner)
