from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    viewers_list = list()
    for customer in customers:
        viewers_list.append(Customer(customer["name"], customer["food"]))
    hall = CinemaHall(hall_number)
    cleaner_staff = Cleaner(cleaner)
    cinema_bar = CinemaBar()
    for viewer_in_bar in viewers_list:
        cinema_bar.sell_product(viewer_in_bar.food, viewer_in_bar)
    hall.movie_session(movie, viewers_list, cleaner_staff)
