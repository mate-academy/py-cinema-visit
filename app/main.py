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
    bar_service = CinemaBar()  # nome mais explícito que 'bar'

    for data in customers:
        cust = Customer(name=data['name'], food=data['food'])
        bar_service.sell_product(customer=cust, product=cust.food)

    hall = CinemaHall(number=hall_number)
    cleaner_obj = Cleaner(cleaner)

    # ✅ chamada corrigida: argumentos posicionais
    hall.movie_session(
        movie,
        [Customer(c['name'], c['food']) for c in customers],
        cleaner_obj,
    )
