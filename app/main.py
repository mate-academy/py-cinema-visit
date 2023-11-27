from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    visitors = []
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cinema_cleaner = Cleaner(cleaner)

    for customer in customers:
        visitors.append(Customer(customer["name"], customer["food"]))

    for visitor in visitors:
        cinema_bar.sell_product(visitor, visitor.food)

    cinema_hall.movie_session(movie, visitors, cinema_cleaner)
