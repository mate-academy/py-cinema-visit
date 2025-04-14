from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list, hall_number: int, cleaner_name: str, movie: str
) -> None:
    # Input validation
    assert isinstance(customers, list), "customers must be a list of dict"
    assert all(
        isinstance(customer, dict) for customer in customers
    ), "each customer must be a dictionary"
    assert isinstance(hall_number, int), "hall_number must be an integer"
    assert isinstance(cleaner_name, str), "cleaner_name must be a string"
    assert isinstance(movie, str), "movie must be a string"

    # Proceed with the logic only if inputs are valid
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner_name)

    customer_instances = [
        Customer(info["name"], info["food"])
        for info in customers
        if "name" in info and "food" in info
    ]

    for customer in customer_instances:
        cinema_bar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie, customer_instances, cleaner)
