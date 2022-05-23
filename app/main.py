from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    visitors = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for visitor in visitors:
        CinemaBar.sell_product(visitor, visitor.food)
    hall.movie_session(movie, visitors, clean)
