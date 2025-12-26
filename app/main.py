from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_visitors = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    hall = CinemaHall(hall_number)
    cleaning_manager = Cleaner(cleaner)

    for visitor in cinema_visitors:
        CinemaBar.sell_product(visitor.food, visitor)

    hall.movie_session(movie, cinema_visitors, cleaning_manager)
