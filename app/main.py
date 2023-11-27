from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    visitors = []

    for customer in customers:
        visitor = Customer(customer["name"], customer["food"])
        visitors.append(visitor)
        CinemaBar.sell_product(visitor, customer["food"])

    cinema_hall.movie_session(movie, visitors, cleaner)
