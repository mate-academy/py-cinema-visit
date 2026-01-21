from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    clean_staff = Cleaner(cleaner)
    geeks = []
    for customer in customers:
        visitor = Customer(customer["name"], customer["food"])
        cinema_bar.sell_product(visitor, visitor.food)
        geeks.append(visitor)

    hall.movie_session(movie, geeks, clean_staff)
