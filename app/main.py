from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    current_hall = CinemaHall(hall_number)
    current_cleaner = Cleaner(cleaner)
    visitors_list = []
    for visitorb in customers:
        current_visitor = Customer(visitorb["name"], visitorb["food"])
        CinemaBar.sell_product(current_visitor, current_visitor.food)
        visitors_list.append(current_visitor)
    current_hall.movie_session(movie, visitors_list, current_cleaner)
