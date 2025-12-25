from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    """
    Simulates a cinema visit: sells food to customers,
    conducts movie session, and cleans the hall.

    Args:
        customers: list of dicts with "name" and "food" keys
        hall_number: number of the hall
        cleaner: name of the cleaner
        movie: movie name
    """
    # Create Customer instances from the provided data
    customer_instances: List[Customer] = []
    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        customer_instances.append(customer)

    # Create CinemaHall instance
    hall = CinemaHall(number=hall_number)

    # Create Cleaner instance
    cleaner_instance = Cleaner(name=cleaner)

    # Cinema bar sells products to customers
    for customer in customer_instances:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    # Cinema hall conducts movie session
    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
