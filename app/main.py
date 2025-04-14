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

    customer_instances = [
        Customer(
            name=customer["name"], food=customer["food"]
        ) for customer in customers
    ]

    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]

hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(
    customers=customers,
    hall_number=hall_number,
    cleaner=cleaner_name,
    movie=movie
)
