from __future__ import annotations
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list[dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customers_list: list[Customer] = []
    for data in customers:
        temp_customer = Customer(name=data["name"], food=data["food"])
        CinemaBar.sell_product(product=temp_customer.food, customer=temp_customer)
        customers_list.append(temp_customer)

    cleaner_hall = Cleaner(name=cleaner)
    hall = CinemaHall(hall_number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner_hall,
    )
