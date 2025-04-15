from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    visitors = [Customer(name=customer["name"], food=customer["food"])
                for customer in customers]
    cinema_hall = CinemaHall(number=hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(name=cleaner)

    for visitor in visitors:
        cinema_bar.sell_product(customer=visitor, product=visitor.food)

    cinema_hall.movie_session(
        movie_name=movie, customers=visitors, cleaner=cleaner
    )
