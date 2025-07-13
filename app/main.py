from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict[str, str]],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    visiters = [
        Customer(name=customer.get("name"), food=customer.get("food"))
        for customer in customers
    ]

    cleaning_staff = Cleaner(name=cleaner)

    hall = CinemaHall(number=hall_number)

    for visiter in visiters:
        CinemaBar.sell_product(visiter.food, visiter)

    hall.movie_session(movie, visiters, cleaning_staff)
