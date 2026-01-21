from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    vievers = []
    for viever in customers:
        vievers.append(Customer(viever["name"], viever["food"]))

    bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for viever in vievers:
        bar.sell_product(viever.food, viever)
    hall.movie_session(movie, vievers, cleaner)
