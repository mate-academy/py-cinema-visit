from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cleaning_staff = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    visitors = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    with hall.movie_session(movie, visitors, cleaning_staff):
        for visitor in visitors:
            visitor.watch_movie(movie)
