from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from typing import List, Dict


def cinema_visit(
    customers: List[Dict[str, str]], hall_number: int,
        cleaner: str, movie: str
) -> None:
    """Simulate a complete cinema visit."""
    # Create Customer instances
    customer_instances = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]

    # Sell food to each customer using CinemaBar
    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # Create CinemaHall and Cleaner instances
    cinema_hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    # Start the movie session
    cinema_hall.movie_session(
        movie_name=movie, customers=customer_instances,
        cleaning_staff=cleaning_staff
    )
