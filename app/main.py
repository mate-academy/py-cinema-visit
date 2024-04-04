from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    clients = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for client in clients:
        CinemaBar.sell_product(client.food, client)

    hall = CinemaHall(hall_number)
    staff = Cleaner(cleaner)

    hall.movie_session(movie, clients, staff)
