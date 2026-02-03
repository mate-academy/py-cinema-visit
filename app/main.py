from __future__ import annotations
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:

    customers_list = []
    cleaner_obj = Cleaner(name=cleaner)
    cinema_hall_obj = CinemaHall(number=hall_number)

    for customer in customers:
        customer_obj = Customer(name=customer["name"], food=customer["food"])
        customers_list.append(customer_obj)
        CinemaBar.sell_product(
            customer=customer_obj,
            product=customer_obj.food
        )
    cinema_hall_obj.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner_obj
    )
