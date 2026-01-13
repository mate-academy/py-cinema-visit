from __future__ import annotations
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customer_objects = [
        Customer(name=customer["name"],
                 food=customer["food"])
        for customer in customers]
    for customer in customer_objects:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer
        )
    cleaner_object = Cleaner(name=cleaner)
    hall_object = CinemaHall(number=hall_number)

    hall_object.movie_session(movie_name=movie,
                              customers=customer_objects,
                              cleaning_staff=cleaner_object)
