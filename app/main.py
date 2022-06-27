from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    visitors = []
    # making visitors list
    for visitor in customers:
        visitors.append(Customer(visitor["name"], visitor["food"]))
    # visitors are going to the bar
    visitor_in_bar = CinemaBar()
    for visitor in visitors:
        visitor_in_bar.sell_product(visitor.food, visitor)
    # movie session
    CinemaHall(hall_number).movie_session(movie, visitors, Cleaner(cleaner))
