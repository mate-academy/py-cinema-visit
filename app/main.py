from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: List[Dict[str, str]], hall_number: int,
        cleaner: str, movie: str
) -> None:
    customer_instances = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    cb = CinemaBar()
    for customer in customer_instances:
        cb.sell_product(customer.food, customer)

    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customer_instances, Cleaner(cleaner))


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers, hall_number=hall_number,
             cleaner=cleaner_name, movie=movie)
