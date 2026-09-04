from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list, hall_number: int,
                 cleaner_name: str, movie: str) -> None:

    cleaner = Cleaner(cleaner_name)

    hall = CinemaHall(hall_number)

    viewers = []

    for customer in customers:
        viewer = Customer(customer["name"], customer["food"])
        viewers.append(viewer)

        CinemaBar.sell_product(viewer.food, viewer)

    hall.movie_session(movie_name=movie, customers=viewers,
                       cleaning_staff=cleaner)
