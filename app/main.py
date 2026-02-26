from typing import List, Dict

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:

    cinema_hall = CinemaHall(number=hall_number)
    cleaner_staff = Cleaner(name=cleaner)

    customer_objects = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]

    for customer in customer_objects:
        CinemaBar.sell_product(   # 👈 chamada estática correta
            customer=customer,
            product=customer.food,
        )

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_staff,
    )
