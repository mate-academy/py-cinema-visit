from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int,
        cleaner: str, movie: str) -> None:
    viewers = []

    for viewer in customers:
        viewers.append(Customer
                       (viewer["name"],
                        viewer["food"])
                       )
    bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for viewer in viewers:
        bar.sell_product(viewer.food, viewer)
    hall.movie_session(movie, viewers, cleaner)
