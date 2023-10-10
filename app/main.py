# write your imports here
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie_name: str
) -> None:
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    visitors = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for visitor in visitors:
        CinemaBar.sell_product(visitor.food, visitor)

    hall.movie_session(movie_name, visitors, cleaner)
