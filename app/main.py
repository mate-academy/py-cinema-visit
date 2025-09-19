from __future__ import annotations
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    movie: str,
    customers: list,
    hall_number: int,
    cleaner: str,
) -> None:

    customers_list = []
    for customer in customers:
        temp_customer = Customer(name=customer["name"], food=customer["food"])
        CinemaBar.sell_product(product=temp_customer.food, customer=temp_customer)
        customers_list.append(temp_customer)

    cleaner_hall = Cleaner(cleaner)
    hall = CinemaHall(hall_number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner_hall,
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
        movie=movie,
        customers=customers,
        hall_number=hall_number,
        cleaner=cleaner_name,
    )
