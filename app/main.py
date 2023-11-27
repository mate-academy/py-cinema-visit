from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    bar = CinemaBar()
    hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)

    visitors = [Customer(visitor['name'], visitor['food'])
                for visitor in customers]
    for visitor in visitors:
        bar.sell_product(visitor.food, visitor)
    hall.movie_session(movie, visitors, clean)
