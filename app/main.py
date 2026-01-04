from typing import List, Dict

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers_data: List[Dict[str, str]],
        hall_number: int,
        cleaner_name: str,
        movie_name: str
) -> None:

    customers = []

    for data in customers_data:
        customer = Customer(name=data["name"], food=data["food"])
        customers.append(customer)

        CinemaBar.sell_product(
            product=data["food"],
            customer=customer
        )

    cleaner = Cleaner(name=cleaner_name)
    hall_instance = CinemaHall(number=hall_number)

    hall_instance.movie_session(
        movie_name=movie_name,
        customers=customers,
        cleaning_staff=cleaner
    )


if __name__ == "__main__":
    customers_data = [
        {"name": "Bob", "food": "popcorn"},
        {"name": "Alice", "food": "Coca-cola"},
    ]

    cinema_visit(
        customers_data=customers_data,
        hall_number=1,
        cleaner_name="John",
        movie_name="Dune"
    )
