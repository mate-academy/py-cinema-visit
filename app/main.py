from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str, movie: str
) -> None:
    visitors = [
        Customer(customer.get("name"),
                 customer.get("food"))
        for customer in customers
    ]
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for visitor in visitors:
        CinemaBar.sell_product(visitor, visitor.food)
    hall.movie_session(movie, visitors, cleaner)
