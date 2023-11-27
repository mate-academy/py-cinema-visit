from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str):
    spectators = []
    for customer in customers:
        spectators.append(Customer(name=customer["name"],
                                   food=customer["food"]))

    cinema_bar = CinemaBar()
    for spectator in spectators:
        cinema_bar.sell_product(spectator, spectator.food)

    cleaner = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie_name=movie,
                              customers=spectators,
                              cleaning_staff=cleaner)
