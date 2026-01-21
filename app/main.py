from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    clients = []

    for customer in customers:
        person = Customer(name=customer["name"])
        clients.append(person)
        CinemaBar.sell_product(person, product=customer["food"])

    cinema_hall.movie_session(movie_name=movie,
                              customers=clients,
                              cleaning_staff=cleaner)
