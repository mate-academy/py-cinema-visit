from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    visitors = [Customer(item["name"], item["food"]) for item in customers]

    for visitor in visitors:
        CinemaBar.sell_product(customer=visitor, product=visitor.food)

    hall = CinemaHall(hall_number)
    hall.movie_session(movie, visitors, Cleaner(cleaner))
