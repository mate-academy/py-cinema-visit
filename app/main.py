from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    hall_n = CinemaHall(hall_number)
    clean_man = Cleaner(cleaner)
    clients = []
    for client in customers:
        cl = Customer(client.get("name"), client.get("food"))
        clients.append(cl)
        CinemaBar.sell_product(cl.food, cl)
    hall_n.movie_session(movie, clients, clean_man)
