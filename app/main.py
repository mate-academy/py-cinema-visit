from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list[dict], hall_number: int, cleaner: str, movie: str
) -> None:
    visitors = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    staff = Cleaner(cleaner)

    for visitor in visitors:
        cinema_bar.sell_product(visitor.food, visitor)
    cinema_hall.movie_session(movie, visitors, staff)
