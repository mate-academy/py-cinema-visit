from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from typing import List, Dict


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    # создаём объекты
    customer_objs: List[Customer] = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]
    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    # бар продаёт еду
    for customer in customer_objs:
        cinema_bar.sell_product(
            product=customer.food,
            customer=customer,
        )

    # киносеанс
    hall.movie_session(
        movie_name=movie,
        customers=customer_objs,
        cleaning_staff=cleaner_obj,
    )
