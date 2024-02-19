from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:

    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_name = Cleaner(cleaner)
    cinema_visitors = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for visitor in cinema_visitors:
        cinema_bar.sell_product(visitor.food, visitor)

    hall.movie_session(movie, cinema_visitors, cleaner_name)
