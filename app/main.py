from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_bar = CinemaBar()
    clients = [Customer(*client.values()) for client in customers]
    cinema_hall = CinemaHall(hall_number)
    current_cleaner = Cleaner(cleaner)
    for client in clients:
        cinema_bar.sell_product(client.food, client)
    cinema_hall.movie_session(movie, clients, current_cleaner)
