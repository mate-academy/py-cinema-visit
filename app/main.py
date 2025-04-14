from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    visitors = []
    for customer in customers:
        visitors.append(Customer(customer["name"], customer["food"]))
    for visitor in visitors:
        CinemaBar.sell_product(visitor, visitor.food)
    hall = CinemaHall(hall_number)
    clean_staff = Cleaner(cleaner)
    hall.movie_session(movie, visitors, clean_staff)
