from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    visitors = [
        Customer(
            name=customer["name"],
            food=customer["food"]
        ) for customer in customers
    ]
    hall_number = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for visitor in visitors:
        CinemaBar.sell_product(visitor.food, visitor)
    hall_number.movie_session(
        movie_name=movie,
        customers=visitors,
        cleaning_stuff=cleaner
    )
