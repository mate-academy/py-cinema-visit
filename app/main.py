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
    """
    Simulates a visit to the cinema.

    Parameters:
    customers (list): A list of dictionaries, where each dictionary
    represents a customer and contains 'name' and 'food' keys.
    hall_number (int): The number of the hall where the movie will be shown.
    cleaner (str): The name of the cleaner.
    movie (str): The name of the movie to be shown.
    """

    name_and_food = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    name_cleaner = Cleaner(cleaner)

    for customer in name_and_food:
        cinema_bar.sell_product(customer.food, customer)

    hall.movie_session(movie, name_and_food, name_cleaner)
