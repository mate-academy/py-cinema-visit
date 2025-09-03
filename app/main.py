from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    visitors = list()
    for customer in customers:
        visitors.append(Customer(customer["name"], customer["food"]))
    hall = CinemaHall(hall_number)
    cleaner_staff = Cleaner(cleaner)
    for visitor in visitors:
        CinemaBar.sell_product(visitor, visitor.food)
    hall.movie_session(movie, visitors, cleaner_staff)

