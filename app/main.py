from __future__ import annotations
from typing import Iterable, Union

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import CinemaStaff


def _as_customer(obj: Union[Customer, dict]) -> Customer:
    if isinstance(obj, Customer):
        return obj
    # Esperado: dict com chaves 'name' e 'food'
    return Customer(name=obj["name"], food=obj["food"])


def _as_staff(obj: Union[CinemaStaff, str, dict]) -> CinemaStaff:
    if isinstance(obj, CinemaStaff):
        return obj
    if isinstance(obj, str):
        return CinemaStaff(name=obj)
    # Se vier dict com 'name'
    return CinemaStaff(name=obj["name"])


# ✅ Assinatura EXATA exigida
def cinema_visit(movie: str, customers: Iterable[Union[Customer, dict]], hall_number: int, cleaner: Union[CinemaStaff, str, dict]) -> None:
    # ✅ Construir UMA lista reutilizável de customers
    customer_objs = [_as_customer(c) for c in customers]

    # ✅ NÃO instanciar CinemaBar; chamar no class object
    for c in customer_objs:
        CinemaBar.sell_product(product=c.food, customer=c)

    # ✅ Reusar customer_objs na sessão do hall
    cleaner_obj = _as_staff(cleaner)
    hall = CinemaHall(hall_number=hall_number)
    hall.movie_session(movie_name=movie, customers=customer_objs, cleaning_staff=cleaner_obj)
