from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    visitors = []
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    bar_cinema = CinemaBar()
    for customer in customers:
        visitor = Customer(customer["name"], customer["food"])
        visitors.append(visitor)
        bar_cinema.sell_product(visitor, visitor.food)
    hall.movie_session(movie, visitors, cleaner)
