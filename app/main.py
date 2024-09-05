from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict[str, str]],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    """
    Simulates a visit to the cinema, where customers buy food,
    watch a movie, and the hall is cleaned.

    Args:
        customers (list[dict[str, str]]):
            A list of dictionaries where each dictionary represents a customer,
            containing 'name' (str) and 'food' (str) keys.
        hall_number (int): The number of the cinema hall.
        cleaner (str):
            The name of the cleaner responsible for cleaning the hall.
        movie (str): The name of the movie being shown.

    Workflow:
        1. Create a list of Customer instances based on the input data.
        2. Create an instance of CinemaHall using the given hall number.
        3. Create an instance of Cleaner using the cleaner's name.
        4. Create an instance of CinemaBar to handle selling products.
        5. Cinema bar sells food to each customer.
        6. Start the movie session in the cinema hall,
            where customers watch the movie.
        7. After the movie ends, the cleaner cleans the cinema hall.
    """
    customers_list: list[Customer] = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cleaner_staff = Cleaner(cleaner)
    cinema_bar = CinemaBar()

    for customer in customers_list:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customers_list, cleaner_staff)
