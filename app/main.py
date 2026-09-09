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
    visitors = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    hall = CinemaHall(hall_number)
    hall_cleaner = Cleaner(cleaner)

    for visitor in visitors:
        CinemaBar.sell_product(product=visitor.food, customer=visitor)

    hall.movie_session(movie, visitors, hall_cleaner)
