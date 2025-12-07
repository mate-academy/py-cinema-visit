from typing import List, Dict

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:

    customer_instances = []

    cinema_bar = CinemaBar()

    for cust_data in customers:
        customer = Customer(name=cust_data["name"], food=cust_data["food"])
        customer_instances.append(customer)
        cinema_bar.sell_product(customer=customer, product=customer.food)

    cleaner_instance = Cleaner(name=cleaner)
    hall_instance = CinemaHall(number=hall_number)

    hall_instance.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )


if __name__ == "__main__":
    customers_data = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    hall_num = 5
    cleaner_name = "Anna"
    movie = "Madagascar"

    cinema_visit(
        customers=customers_data,
        hall_number=hall_num,
        cleaner=cleaner_name,
        movie=movie
    )
