# app/main.py

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    movie: str,
    customers: list[dict],
    hall_number: int,
    cleaner: str,
) -> None:
    """
    Simulate a cinema visit:
    - Sell food to customers
    - Run movie session
    - Cleaner cleans hall
    """
    # Create Customer instances
    customer_objects = [
        Customer(name=c["name"], food=c["food"])
        for c in customers
    ]

    # Sell products to customers
    for cust in customer_objects:
        CinemaBar.sell_product(
            product=cust.food,
            customer=cust,
        )

    # Create hall and cleaner
    hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    # Run movie session
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff,
    )


if __name__ == "__main__":
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"},
    ]
    hall_number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"

    cinema_visit(
        customers=customers,
        hall_number=hall_number,
        cleaner=cleaner_name,
        movie=movie,
    )
