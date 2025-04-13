from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    cb = CinemaBar
    ch = CinemaHall(hall_number)
    list_customer = [Customer(custom["name"], custom["food"])
                     for custom in customers]
    clean = Cleaner(cleaner)
    for value in list_customer:
        cb.sell_product(value, value.food)
    ch.movie_session(movie, list_customer, clean)
