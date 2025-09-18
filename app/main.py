from typing import Iterable

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: Iterable[dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    """Executa o fluxo da visita ao cinema imprimindo cada etapa."""
    bar_service = CinemaBar()  # nome mais explícito que 'bar'
    customer_objs: list[Customer] = []

    for data in customers:
        cust = Customer(name=data['name'], food=data['food'])
        bar_service.sell_product(customer=cust, product=cust.food)
        customer_objs.append(cust)

    hall = CinemaHall(number=hall_number)
    cleaner_obj = Cleaner(cleaner)

    hall.movie_session(
        movie=movie,
        customers=customer_objs,
        cleaner=cleaner_obj,
    )
