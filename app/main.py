from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    ch = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for customer in customers:
        CinemaBar.sell_product(
            customer=Customer(customer["name"], customer["food"]),
            product=customer["food"]
        )
    ch.movie_session(
        movie_name=movie,
        customers=[
            Customer(customer["name"], customer["food"])
            for customer in customers
        ],
        cleaning_staff=cleaner
    )
