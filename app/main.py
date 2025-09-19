from __future__ import annotations
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list[dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customers_list: list[Customer] = []
    for customer in customers:
        temp_customer = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(
            customer=temp_customer,
            product=temp_customer.food
        )
        customers_list.append(temp_customer)

    cleaner_hall = Cleaner(cleaner)

    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customers_list, cleaner_hall)


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
