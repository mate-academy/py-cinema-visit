from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    bar = CinemaBar()
    all_visitors = []
    for visitor in customers:
        new_visitor = Customer(visitor["name"], visitor["food"])
        all_visitors.append(new_visitor)
        bar.sell_product(new_visitor.food, new_visitor)

    hall = CinemaHall(hall_number)
    cleaner_name = Cleaner(cleaner)
    hall.movie_session(movie, all_visitors, cleaner_name)
