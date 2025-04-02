from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    visitors = [Customer(
        customer["name"],
        customer["food"])
        for customer in customers]
    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)
    for visitor in visitors:
        cinema_bar.sell_product(visitor.food, visitor)
    hall.movie_session(movie, visitors, cleaner)
