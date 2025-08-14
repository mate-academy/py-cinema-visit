from typing import List
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: List[dict],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    """Simulate a cinema visit."""
    customer_objects = [
        Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        for customer_data in customers
    ]

    for customer in customer_objects:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer
        )

    hall = CinemaHall(hall_number=hall_number)
    cleaner_obj = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_obj
    )
