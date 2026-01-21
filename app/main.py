from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    clients = []
    for value in customers:
        client = Customer(value["name"], value["food"])
        clients.append(client)

    for client in clients:
        CinemaBar.sell_product(client, client.food)

    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    hall.movie_session(movie, clients, cleaner)
