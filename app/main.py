from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    visitors = []
    for customer in customers:
        visitors.append(Customer(customer["name"], customer["food"]))

    cinema_bar = CinemaBar()
    for visitor in visitors:
        cinema_bar.sell_product(visitor, visitor.food)

    cleaner = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)

    cinema_hall.movie_session(movie, visitors, cleaner)
