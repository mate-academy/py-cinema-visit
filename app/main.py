from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    visitors = [
        Customer(visitor["name"], visitor["food"])
        for visitor in customers
    ]
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    hall_cleaner = Cleaner(cleaner)

    for visitor in visitors:
        cinema_bar.sell_product(visitor, visitor.food)
    cinema_hall.movie_session(movie, visitors, hall_cleaner)
