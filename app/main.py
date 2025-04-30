from __future__ import annotations
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    new_customers = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    hall = CinemaHall(number=hall_number)
    new_cleaner = Cleaner(name=cleaner)
    cinema_bar = CinemaBar()

    for customer in new_customers:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    hall.movie_session(
        movie_name=movie,
        customers=new_customers,
        cleaning_staff=new_cleaner
    )
