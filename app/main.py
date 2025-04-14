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
    # Create Customer instances
    customer_instances = [Customer(cust['name'], cust['food']) for cust in customers]

    # Sell products to customers
    for customer in customer_instances:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    # Create CinemaHall and Cleaner instances
    hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    # Start movie session
    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )