from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    hall = CinemaHall(hall_number)
    clients = []

    for i in range(len(customers)):
        clients.append(Customer(customers[i]["name"], customers[i]["food"]))
        CinemaBar.sell_product(clients[i].food, clients[i])

    hall.movie_session(movie, clients, Cleaner(cleaner))
