from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    clients = [
        Customer(client["name"], client["food"]) for client in customers
    ]

    for client in clients:
        CinemaBar.sell_product(client.food, client)

    name_cleaner = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)

    cinema_hall.movie_session(movie, clients, name_cleaner)
