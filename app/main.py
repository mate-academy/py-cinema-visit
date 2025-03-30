from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str):

    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    list_customers = []
    for costumer in customers:
        viewer = Customer(costumer["name"], costumer["food"])
        list_customers.append(viewer)
        cinema_bar.sell_product(viewer, viewer.food)
    cinema_hall.movie_session(movie, list_customers, clean)
