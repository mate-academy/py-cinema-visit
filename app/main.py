from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str,
                 movie: str) -> None:
    visitors = []
    for customer in customers:
        visitors.append(Customer(customer["name"], customer["food"]))
    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    clean = Cleaner(cleaner)
    for visitor in visitors:
        cinema_bar.sell_product(visitor.food, visitor)
    hall.movie_session(movie, visitors, clean)
