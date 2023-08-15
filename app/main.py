from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):

    visitors = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    cinema_hall = CinemaHall(hall_number)
    cleaner_staff = Cleaner(cleaner)

    for visitor in visitors:
        CinemaBar.sell_product(visitor, visitor.food)

    cinema_hall.movie_session(movie, visitors, cleaner_staff)
