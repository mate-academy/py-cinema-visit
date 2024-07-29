from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        number: int,
        cleaner: str,
        movie: str
) -> None:
    list_visitors = []
    for customer in customers:
        visitor = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(visitor.food, visitor)
        list_visitors.append(visitor)

    CinemaHall(number).movie_session(movie, list_visitors, Cleaner(cleaner))
