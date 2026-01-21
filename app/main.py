from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = [
        Customer(guest["name"], guest["food"])
        for guest in customers]
    cb = CinemaBar()
    for person in customers_list:
        cb.sell_product(
            customer=person,
            product=person.food)
    CinemaHall(hall_number).movie_session(
        movie,
        customers_list,
        Cleaner(cleaner)
    )
