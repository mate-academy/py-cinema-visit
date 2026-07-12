from __future__ import annotations

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customer_objects = []

    for customer_data in customers:
        customer_objects.append(Customer(name=customer_data["name"],
                                         food=customer_data["food"]))

    hall = CinemaHall(number=hall_number)
    cleaner_obj = Cleaner(name=cleaner)

    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food,
                               customer=customer)

    hall.movie_session(movie_name=movie,
                       customers=customer_objects,
                       cleaning_staff=cleaner_obj)
